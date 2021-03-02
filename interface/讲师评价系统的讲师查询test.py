import requests
import unittest

class testTeacher(unittest.TestCase):
    def testFindAllTeacher(self):
        #准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllTeacher"
        data = {}

        expect = 200 #期望数据
        #调用被测接口
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"

        #提取状态码和响应数据
        code = response.status_code
        txt = response.text

        #断言
        print(txt)
        self.assertEqual(expect,code)

    def testLogin(self):
        #准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet"
        data = {
            "method":"login",
            "loginname": "stars",
            "password":"123456"
        }
        expect = "菜单"
        #调用被测接口
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        data = response.text
        #断言
        self.assertIn(expect,data)

    def testFindAllMenu(self):
        url="http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllMenu"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)


    def testFindAllPicture(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllPicture"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testFindAllStudent(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testFindAllTeacherMenu(self):
        url = "http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllTeacherMenu"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testFindAllCourse(self):
        url = "http://www.jasonisoft.cn:8080/HKR/CourseServlet?method=findAllCourse"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testGetTodayAllEvaluate(self):
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=getTodayAllEvaluate"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testReportAll(self):
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=reportAll"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)
























