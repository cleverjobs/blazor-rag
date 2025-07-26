# TreeView indent

## Question

**Ant** asked on 08 Apr 2024

Is it possible to increase the indent on child folder items?

## Answer

**Dimo** answered on 11 Apr 2024

Hello Anthony, Yes, you can use custom CSS to override our theme and increase the TreeView item indentation: <TelerikTreeView Class="more-indent" /> <style>.more-indent.k-treeview-item.k-treeview-item { margin-left: 24px;
} </style> If you remove the custom CSS class, the CSS rule will target all TreeViews. Regards, Dimo Progress Telerik
