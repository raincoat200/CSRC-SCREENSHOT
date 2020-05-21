# CSRC-SCREENSHOT
证券期货市场失信记录批量查询及截图工具,支持OCR验证码识别.   

![运行日志截图](https://github.com/raincoat200/CSRC-SCREENSHOT/blob/master/log.jpg)  

## 实现功能:
    
   1. 加载查询队列身份信息  
   
        `拟支持EXCEL或JSON数据源格式`
    
   2.  打开WEB页面,循环提交查询信息   
   
        `chrome 无痕模式,批量爬虫`   
        
   3. 对接打码平台 
    
        `自动识别验证码,识别错误的逻辑处理?`

   4. 文件管理   
   
        `截图获取信用页面,重命名截图.根据自定义规则归档到指定路径`

   5. 回传TFTP服务器   
        `根据业务需要,回传到业务系统TFTP服务器指定目录`

## 完成进度:
- [x] 验证码对接打码平台识别
- [x] 爬虫模块定位及功能实现
- [x] 截图生成的有效性及文件管理
- [ ] 身份信息数据API导入接口
- [ ] 回传TFTP模块
- [ ] 数据源自动爬虫,以实现整套业务流的自动化
