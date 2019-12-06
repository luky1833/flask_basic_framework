# ecdata-cmp-py
    简称：ecdata Cloud management platforms  简称 ecdata-cmp
    
    python版本:3.6.4
    代码框架:flask
      
## 项目代码
    # 代码仓库地址
    git clone git@code.aliyun.com:ecdata/ecdata-cmp-py.git
    # 文件路径
    cd ecdata-cmp-py
## 介绍
### 注意事项
    1.编码风格：https://segmentfault.com/a/1190000018035361
### 项目架构
    |-flasky
        |-app/
            |-templates/
            |-static/
            |-main/
                |-__init__.py
                |-errors.py
                |-forms.py
                |-views.py
            |-controller/
                |-__init__.py
                |-logger.py
                |-base.py
            |-api/
                |-__init__.py
                |-blue_print.py
            |-__init__.py
            |-email.py
            |-models.py
        |-migrations/
        |-tests/
            |-__init__.py
            |-test*.py
        |-requirements.txt
        |-config.ini #配置文件
        |-manage.py #启动文件
        |-README.md
        |-Dockerfile #docker 配置文件
### 启动步骤
    python manage.py
