# 更新说明

## [v2.1.1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/2.1.1)
- 修复访问model子链接时，菜单激活状态渲染问题
- 修复时间范围过滤器逻辑，在过滤取消焦点时，将时间筛选置空

## [v2.1.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/2.1.0)
- 新增基于daterangepicker的时间过滤器
- 为所有的filter新增min-width样式
- 调整change_list视图object-tools的位置，与actions处于同一行
- 更新locale
- 在服务器端计算菜单的活跃状态，原来通过js在浏览器实现

## [v2.0.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/2.0.0)
- 移除 `django-treebeard` 依赖包, 同时修复 #28, #29, #30
- 移除了所有models，不再通过数据库的方式管理自定义菜单及其他选项
- 所有特性均通过继承`core.AdminLteConfig`类来实现