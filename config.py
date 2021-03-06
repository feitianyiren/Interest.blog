# -*- coding:utf8 -*-

import os

GLOBAL={

    "Host": os.getenv("Interest_blog_Host", "0.0.0.0"),
    #Application run network address, you can set it `0.0.0.0`, `127.0.0.1`, or someone IP

    "Port": int(os.getenv("Interest_blog_Port", 10140)),
    #Application run port, default port

    "LogLevel": os.getenv("Interest_blog_LogLevel", "DEBUG"),
    #Write log's level, current is DEBUG，INFO，WARNING，ERROR，CRITICAL
}

PRODUCT={

    "ProcessName": "Interest.blog",
    #Custom process, you can see it with "ps aux|grep ProcessName"(with setproctitle module)

    "ProductType": os.getenv("Interest_blog_ProductType", "tornado"),
    #Production environment starting method, optional: `gevent`, `tornado`, `uwsgi`
}

SSO={

    "SSO.URL": os.getenv("Interest_blog_SSOURL", "https://passport.saintic.com"),
    #The passport(SSO Authentication System) Web Site URL.

    "SSO.PROJECT": PRODUCT["ProcessName"],
    #SSO request application.
}

PLUGINS={

    "CodeHighlighting": os.getenv("Interest_blog_CodeHighlighting", True),
    #代码高亮插件

    "DuoshuoComment": {
        "enable": os.getenv("Interest_blog_DuoshuoComment_enable", False),
        "shortName": os.getenv("Interest_blog_DuoshuoComment_shortName", "saintic")
    },
    #多说评论插件

    "Weather": os.getenv("Interest_blog_Weather", True),
    #天气显示插件

    "BaiduAutoPush": os.getenv("Interest_blog_BaiduAutoPush", True),
    #百度自动推送插件

    "BaiduActivePush": {
        "enable":  os.getenv("Interest_blog_BaiduActivePush_enable", True),
        "callUrl": os.getenv("Interest_blog_BaiduActivePush_callUrl", "http://data.zz.baidu.com/urls?site=www.saintic.com&token=QbriJ4Iv7TGi8yOF")
    },
    #百度主动推送(实时)插件

    "BaiduStatistics": os.getenv("Interest_blog_BaiduStatistics", True),
    #百度统计插件

    "BaiduShare": os.getenv("Interest_blog_BaiduShare", True),
    #百度分享插件

    "BackupBlog": os.getenv("Interest_blog_BackupBlog", False),
    #备份文章插件

    "UpYunStorage": {
        "enable": os.getenv("Interest_blog_UpYunStorage_enable", False),
        "bucket": os.getenv("Interest_blog_UpYunStorage_bucket", ""),
        "username": os.getenv("Interest_blog_UpYunStorage_username", ""),
        "password": os.getenv("Interest_blog_UpYunStorage_password", ""),
        "secret": os.getenv("Interest_blog_UpYunStorage_secret", ""),
        "timeout": os.getenv("Interest_blog_UpYunStorage_timeout", 10),
        "dn": os.getenv("Interest_blog_UpYunStorage_dn", "https://img.saintic.com"),
        "allow-file-type": "jpg,jpeg,png,gif"
    },
    #又拍云存储插件

    "ChristmasBlessings": os.getenv("Interest_blog_ChristmasBlessings", False),
    #圣诞节祝福插件

    "360AutoPush": os.getenv("Interest_blog_360AutoPush", True),
    #360自动推送插件

    "ShowGitHub": os.getenv("Interest_blog_ShowGitHub", False),
    #个人中心页展现GitHub代码库插件，最多展现49个
}

BLOG={

    "AdminPrefix": os.getenv("Interest_blog_AdminPrefix", "/admin"),
    #后台URI前缀

    "ApiUrl": os.getenv("Interest_blog_ApiUrl", "https://api.saintic.com"),
    #博客API接口地址

    "ExternalSearch": os.getenv("Interest_blog_ExternalSearch", "https://cse.google.com/cse/publicurl?cx=009741766366936003815:jfv5jmieqo8"),
    #站内搜索地址

    #"UpdateRecordId": os.getenv("Interest_blog_UpdateRecordId", 110),

    #"AboutId": os.getenv("Interest_blog_AboutId", 113),

    "openSource": {
        "user": os.getenv("Interest_blog_openSource_user", "staugur"),
        "displayNumber": os.getenv("Interest_blog_openSource_displaynumber", 49),
    },
    #导航-开源项目展现，GitHub用户名
}

MYSQL=os.getenv("Interest_blog_MYSQL", "mysql://host:port:user:password:db")
