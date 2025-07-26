# TreeView roadmap?

## Question

**Alb** asked on 14 Jun 2019

when can we expect to have a TreeView component like this [https://www.syncfusion.com/blazor-components/blazor-treeview](https://www.syncfusion.com/blazor-components/blazor-treeview) Looks like syncfusion already have treeview and much more components for blazor.

## Answer

**Marin Bratanov** answered on 16 Jun 2019

Hello Alberto, The treeview is in our immediate roadmap. In fact, we are already working on it and we will ship it as soon as possible. At the moment, the first concern is compatibility with Preview 6 which brought a lot of breaking changes, however, and I am not sure if the treeview will make in the release that we will ship for compatibility with the framework (hopefully, by the end of the coming week). Even if it doesn't make it into this one, we are committed to a rather aggressive release schedule (perhaps as often as once a month), and the treeview will be available soon. So, I encourage you to follow our releases to get the latest components and fixes: [https://www.telerik.com/support/whats-new/blazor-ui/release-history.](https://www.telerik.com/support/whats-new/blazor-ui/release-history.) You can also do this with a dedicated RSS feed: [https://www.telerik.com/feeds/ui-for-blazor-whats-new.](https://www.telerik.com/feeds/ui-for-blazor-whats-new.) On Syncfusion - they are wrapping jQuery widgets through JS Interop and this is what enables them to provide a lot of components. The downside of this approach is that those components are not native Blazor components and don't really leverage the Blazor framework. We could have done the same with our Kendo UI widgets, but we chose to create everything from the ground up as native Blazor components as we believe this will benefit everyone in the long run, even if it will cause components to take longer to appear in the suite. You can read more on the differences between native components and wrappers in the following post: [https://www.telerik.com/blogs/comparing-native-blazor-components-to-wrapped-javascript-components.](https://www.telerik.com/blogs/comparing-native-blazor-components-to-wrapped-javascript-components.) If you have any outstanding questions, just let me know. Regards, Marin Bratanov

### Response

**Andriy** answered on 15 Jul 2019

Hello Marin How to change vertical space between TreeView nodes? Inside node template I can change anything, but I can't change height of hover style. For example, when i hover cursor on the node, I see more big size rectangle and I want to change this size. Please, look at my screenshot. And please add ThreeView theme in your forum.

### Response

**Andriy** answered on 15 Jul 2019

I found where it was. Early in index.html I change theme from <link rel="stylesheet" href="[https://unpkg.com/@progress/kendo-theme-default@latest/dist/all.css"](https://unpkg.com/@progress/kendo-theme-default@latest/dist/all.css") /> to <link rel="stylesheet" href="[https://unpkg.com/@progress/kendo-theme-bootstrap@latest/dist/all.css"](https://unpkg.com/@progress/kendo-theme-bootstrap@latest/dist/all.css") /> And bootstrap very like big indents.

### Response

**Marin Bratanov** answered on 15 Jul 2019

Hi Andriy, I have created a TreeView sub forum: [https://www.telerik.com/forums/blazor/treeview.](https://www.telerik.com/forums/blazor/treeview.) On altering the built-in appearance of the treeview - in case the various built-in themes ( [https://docs.telerik.com/blazor-ui/themes](https://docs.telerik.com/blazor-ui/themes) ) are not enough, you can also inspect the rendered HTML with the browser dev toolbar and devise CSS rules of your own that will provide the desired changes. For example, the screenshot attached below where the spacing is increased and the hover effect extends more on the sides of the text is achieved with the following code: <style> .k-item.k-treeview-item .k-in { padding: 20px; /* of course, you can tweak the values here as needed by your design, I use 20px all around for brevity */ } </style> @using Telerik.Blazor.Components.TreeView <TelerikTreeView Data="@FlatData"> </TelerikTreeView> @code { public class TreeItem { public int Id { get; set; } public string Text { get; set; } public int? ParentId { get; set; } public bool HasChildren { get; set; } public bool Expanded { get; set; } } public IEnumerable<TreeItem> FlatData { get; set; } protected override void OnInit() { LoadFlatData(); } private void LoadFlatData() { List<TreeItem> items=new List<TreeItem>(); for (int i=1; i <=4; i++) { items.Add(new TreeItem() { Id=i, Text="Category " + i, ParentId=null, HasChildren=i <3, Expanded=true }); } for (int i=5; i <15; i++) { items.Add(new TreeItem() { Id=i, Text="Product " + i, ParentId=i <10? 1: 2 }); } FlatData=items; } } Regards, Marin Bratanov

### Response

**Andriy** answered on 15 Jul 2019

Marin, thank you very much for your advising. Yes, it's works.
