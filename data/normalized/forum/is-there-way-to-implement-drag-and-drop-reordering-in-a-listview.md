# Is there way to implement drag and drop reordering in a ListView?

## Question

**Wil** asked on 08 Apr 2025

I just want to add drag and drop items in a ListView to reorder them. I don't think adding any code or files here will help.

## Answer

**Anislav** answered on 11 Apr 2025

I prepared an example with a grid where drag and drop is enabled. The rows are sorted by index, which you may want to save for future use when the data is loaded again and displayed. There is also a delete button to remove items, and the columns can be merged in case your data is not suitable for display in a tabular format. Here is the example: [https://blazorrepl.telerik.com/cpkyvPFk38QnEKtM36](https://blazorrepl.telerik.com/cpkyvPFk38QnEKtM36) Regards, Anislav Atanasov

### Response

**Will** commented on 11 Apr 2025

Thanks, I can add editing to this, correct?

### Response

**Anislav** commented on 13 Apr 2025

Sure, editing is supported. You can check out the documentation here: [https://www.telerik.com/blazor-ui/documentation/components/grid/editing/overview](https://www.telerik.com/blazor-ui/documentation/components/grid/editing/overview)

### Response

**Anislav** answered on 09 Apr 2025

The ListView component doesn't support drag and drop functionality out of the box. Depending on your requirements, you might consider using Grid, TreeView, or TileLayout instead, as they have builtin drag and drop support and can be customized to look and feel simialr to a list. Could you share a bit more about why you're using ListView? For example, are you relying on its paging features, or do you need to dynamically add or remove items? Regards, Anislav Atanasov

### Response

**Will** commented on 09 Apr 2025

I need to be able to edit and change the order of items. In this use case, order of the items is numbered. I will also need to add and remove items.

### Response

**Hristian Stefanov** answered on 09 Apr 2025

Hi Will, I must admit that drag and drop to reorder is not available for the ListView. We have a feature request about a generic sortable functionality that would cover this. You can follow it if you like. I already voted on your behalf. In the meantime, consider some other Telerik components, which have this feature: ListBox TreeView Regards, Hristian Stefanov

### Response

**Will** commented on 09 Apr 2025

I need to be able to edit and change the order of items. In this use case, order of the items is numbered. I will also need to add and remove items.

### Response

**Hristian Stefanov** commented on 10 Apr 2025

Hi Will, The ListBox component appears to be a good fit for your requirements. It supports reordering items through drag-and-drop or via buttons, and you can easily add or remove items by updating its data collection. Kind Regards, Hristian

### Response

**Will** commented on 10 Apr 2025

I tried the ListBox, but I didn't have access to the textbox and other input controls inside the template.
