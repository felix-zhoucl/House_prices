class PrivateAPIService(BasePrivateApiService):
    """
    动态私有OpenAPI
    使用方法
    get_transfer_form_data
    """

    def execute(self, **kwargs):
        year = kwargs.get("year")
        dept_id = kwargs.get("dept_id")
        try:
            data = self.get_data(year, dept_id)
            # self.log("data:{}".format(data))
            return data
        except Exception as e:
            self.log(traceback.format_exc())
            return {
                "list": [],
                "count": 0
            }

    def get_data(self, year, dept_id):
        """
        获取返回数据
        :param year:
        :param dept_id:
        :return:
        """
        year_begin = "{}-01-01".format(year)
        year_end = "{}-12-31".format(year)
        begin_emp_dict = self.get_emp_data(year_begin, dept_id)
        # self.log("begin_emp_dict:{}".format(begin_emp_dict))
        end_emp_dict = self.get_emp_data(year_end, dept_id)
        # self.log("end_emp_dict:{}".format(end_emp_dict))
        ret = {}
        # 调出
        for emp_id, emp_info in begin_emp_dict.items():
            origin_unit = emp_info.get("unit", {}).get("origin_id")
            end_emp_info = end_emp_dict.get(emp_id)
            if end_emp_info:
                now_unit = end_emp_info.get("unit", {}).get("origin_id")
                if origin_unit != now_unit:
                    emp_info["transfer_type"] = "调出"
                    ret[emp_id] = emp_info
            else:
                emp_info["transfer_type"] = "调出"
                ret[emp_id] = emp_info
        # 调入
        for emp_id, emp_info in end_emp_dict.items():
            origin_unit = emp_info.get("unit", {}).get("origin_id")
            begin_emp_info = begin_emp_dict.get(emp_id)
            if begin_emp_info:
                begin_unit = begin_emp_info.get("unit", {}).get("origin_id")
                if origin_unit != begin_unit:
                    emp_info["transfer_type"] = "调入"
                    ret[emp_id] = emp_info
            else:
                emp_info["transfer_type"] = "调入"
                ret[emp_id] = emp_info

        emp_ids = list(ret.keys())
        job_info_dict = self.get_job_info_dict_by_date(emp_ids, year)
        unit_ids = []
        for emp_id, emp_info in ret.items():
            job_info = job_info_dict.get(emp_id) or {}
            emp_info.update(job_info)
            unit_ids.append(emp_info.get("unit", {}).get("origin_id"))
            unit_ids.append(emp_info.get("new_unit", {}).get("origin_id"))
        unit_parent_dict = self.get_unit_parent_dict(unit_ids)

        return_list = []
        for emp_info in ret.values():
            if emp_info.get("action_reason", {}).get("name") in ["离职", "劳动合同制员工入职", "再入职"]:
                continue
            if emp_info.get("unit", {}).get("origin_id") == emp_info.get("new_unit", {}).get("origin_id"):
                continue
            emp_info["unit_parent"] = unit_parent_dict.get(emp_info.get("unit", {}).get("origin_id"))
            emp_info["new_unit_parent"] = unit_parent_dict.get(emp_info.get("new_unit", {}).get("origin_id"))
            return_list.append(emp_info)

        return {
            "list": return_list,
            "count": len(return_list)
        }

    def get_unit_parent_dict(self, unit_ids):
        """

        :param unit_ids:
        :return:
        """
        param = {
            "model": "OrgUnit",
            "filter_dict": {
                "id": unit_ids
            },
            "page_size": 9999,
            "page_index": 1
        }
        result = self.call_open_api("hcm.model.list", param)["list"]
        return {x.get("id"): x.get("parent", {}).get("name") for x in result}

    def get_job_info_dict_by_date(self, emp_ids, year) -> dict:
        """
        根据年度获取人员任职字典
        :param emp_ids:
        :param year:
        :return:
        """
        ret = {}
        year_begin = "{}-01-01".format(year)
        year_end = "{}-12-31".format(year)
        # 年初
        begin_dict = self.get_job_info_dict(emp_ids, year_begin)
        end_dict = self.get_job_info_dict(emp_ids, year_end)
        for emp_id in emp_ids:
            ret[emp_id] = begin_dict.get(emp_id) or {}
            end_info = end_dict.get(emp_id) or {}

            end_info["new_unit"] = end_info.get("unit")
            end_info["new_department"] = end_info.get("department")
            end_info["new_position"] = end_info.get("position")
            end_info["new_job_step"] = end_info.get("job_step")
            del end_info["unit"]
            del end_info["department"]
            del end_info["position"]
            del end_info["job_step"]

            # if emp_id == 4077981:
            #     self.log("end_info:{}".format(end_info))
            #     self.log("ret[emp_id]:{}".format(ret[emp_id]))

            ret[emp_id].update(end_info)
        return ret

    def get_job_info_dict(self, emp_ids, date_):
        param = {
            "model": "JobInformation",
            "filter_dict": {
                "position_type": 1,
                "employee_id": emp_ids,
                "begin_date": {
                    "lte": date_
                },
                "end_date": {
                    "gte": date_
                }
            },
            "page_size": 99999,
            "page_index": 1,
            "extra_property": {
                "fields": [
                    {"key": "begin_date", "field": ["begin_date"]},
                    {"key": "employee_id", "field": ["employee_id"]},
                    {"key": "action_reason", "field": ["action_reason", "name"]},
                    {"key": "unit", "field": ["unit", "origin_id"]},
                    {"key": "department", "field": ["department", "origin_id"]},
                    {"key": "position", "field": ["position", "origin_id"]},
                    {"key": "unit", "field": ["unit"]},
                    {"key": "department", "field": ["department", "name"]},
                    {"key": "position", "field": ["position", "name"]},
                    {"key": "position", "field": ["job_step", "name"]}
                ]
            }
        }
        # self.log("param:{}".format(param))
        result = self.call_open_api("hcm.model.list", param)["list"]
        ret = {x.get("employee_id"): x for x in result}
        return ret

    def get_emp_data(self, date_, dept_id):
        """
        获取当前时间在本单位下在职的人员
        :param date_:
        :param dept_id:
        :return:
        """
        param = {
            "model": "Employee",
            "filter_dict": {
                "date_": date_,
                "job_info.position_tye": 1,
                "job_info.on_job": 1,
                "department.origin_id": {
                    "child_include": dept_id
                }
            },
            "page_size": 99999,
            "page_index": 1,
            "extra_property": {
                "state": "inside_laborall",
                "fields": [
                    {"key": "name", "field": ["name"]},
                    {"key": "number", "field": ["number"]},
                    {"key": "u_enter_tower_time", "field": ["u_enter_tower_time"]},
                    {"key": "gender", "field": ["gender"]},
                    {"key": "identity_card", "field": ["identity_card"]},
                    {"key": "birthday", "field": ["birthday"]},
                    {"key": "age_count", "field": ["age_count"]},
                    {"key": "unit", "field": ["unit", "origin_id"]},
                    {"key": "unit", "field": ["unit"]},
                    {"key": "department", "field": ["department", "origin_id"]},
                    {"key": "position", "field": ["position", "origin_id"]},
                    {"key": "unit", "field": ["unit", "name"]},
                    {"key": "department", "field": ["department", "name"]},
                    {"key": "position", "field": ["position", "name"]},
                    {"key": "birth_place", "field": ["birth_place"]}
                ]
            }
        }
        result = self.call_open_api("hcm.model.list", param)["list"]
        return {x.get("id"): x for x in result}

    @staticmethod
    def log(log_content):
        """
        日志记录
        :param log_content: 记录内容
        :return:
        """
        log_info = {"log_type": str('get_transfer_form_data'),
                    "create_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "content": str(log_content)}
        CustomerUtil.call_open_api("hcm.model.create", {"model": "dynamic_log", "info": log_info})
