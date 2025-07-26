# Css on HierarchicalData

## Question

**Gia** asked on 13 Oct 2020

Hi I'm using treeview with Hierarchical data Is it possible change the css for the text ? I need to change some char (color/bold) in some text near the icon. Otherwise how is possibile to use the template with a list of item with parentid ? Tnx

## Answer

**Marin Bratanov** answered on 13 Oct 2020

Hi Giampaolo, You can have a different template for the different levels of the treeview, and there you can render whatever class you need. You can read more about this in the following article from the documentation (that particular section is "Multiple Level Bindings" near the end, but the rest can be helpful too): [https://docs.telerik.com/blazor-ui/components/treeview/data-binding/overview.](https://docs.telerik.com/blazor-ui/components/treeview/data-binding/overview.) That article will also explain the general concepts of data binding a treeview, and then you can find more details and examples for the two binding modes in these articles: flat data (ID-ParentID combination): [https://docs.telerik.com/blazor-ui/components/treeview/data-binding/flat-data](https://docs.telerik.com/blazor-ui/components/treeview/data-binding/flat-data) hierarchical data (nested collections of models): [https://docs.telerik.com/blazor-ui/components/treeview/data-binding/hierarchical-data](https://docs.telerik.com/blazor-ui/components/treeview/data-binding/hierarchical-data) Regards, Marin Bratanov
