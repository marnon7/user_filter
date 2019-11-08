运行环境 python3.6+

依赖：
pip install openpyxl 


把用户的检测名单放在dv_input/client, 必须是xlsx格式, 

把dv的检测结果放在dv_input/dv, csv格式

如果是第一次运行需要建好文件夹：

python init.py 

运行

python main.py

运行结果在dv_output/dv, 目录结构和dv_input/dv一致, 是dv增益的部分

### 2019/11/07 增加删除af结果与datavisor结果重合用户的功能

1. 如果是第一次运行,需要执行初始化脚本以建好文件夹：
    
    ```python init.py ```

2. 将af数据放在 `data/input/af` 路径下，将datavisor的报告 放在`data/input/datavisor`路径下

3. 执行主程序:
    
    ```python af_user_filter.py```

运行结果在 `data/output/` 路径下, 目录结构和 `input` 一致
