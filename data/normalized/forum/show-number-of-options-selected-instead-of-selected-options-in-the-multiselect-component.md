# Show number of options selected instead of selected options in the multiselect component

## Question

**Sus** asked on 26 Jan 2022

Hello, In the Telerik multiselect, when I select some options in my multiselect, the multiselect div expands and the display doesn't look good. So I now just want to show the number of options selected instead of the options selected. I looked for it but could not find some solutions regarding it. For ex, lets say there are the following options in the multiselect: One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten. Now when I select One, Five and Seven from the multiselect dropdown, I want the text inside the multiselect component to be " 3 selected ". Is there any workaround for it? Thanks, Susan

## Answer

**Marin Bratanov** answered on 30 Jan 2022

Hello Susan, You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1498325-add-a-tag-mode-summary-tag-mode.](https://feedback.telerik.com/blazor/1498325-add-a-tag-mode-summary-tag-mode.) I've added your Vote for you and clicking the Follow button will subscribe you for email notifications. You can also find a workaround there you can consider and try. You may also find interesting this feature idea too: [https://feedback.telerik.com/blazor/1528556-tagtemplate-for-multi-select.](https://feedback.telerik.com/blazor/1528556-tagtemplate-for-multi-select.) Regards, Marin Bratanov

### Response

**Susan** commented on 02 Feb 2022

Hello there, Thank you for the response. I tried the approach you suggested. But it also could not fulfill the requirements I have. Below is the code I am currently using. Here, I could not select or unselect all the checkboxes without reopening the multiselect again. On clicking the select all button, the value gets updated but in the dropdown, it is not instantly reflected. It is reflected only after closing the multiselect dropdown and again reopening it. Code: @page "/ms" <TelerikMultiSelect Data="@Products" Class="single-tag-mode" @bind-Value="@SelectedProductIDs" AutoClose="false" ValueField="@nameof(Product.ProductID)" TextField="@nameof(Product.ProductName)" Placeholder="Select Products"> <HeaderTemplate> <div @onclick="@(e=> OnCheckboxDivClick(e, 0))"> <input type="checkbox" id="@("checkbox0")" class="k-checkbox" checked="@AllChecked"/> @(AllChecked ? "UnSelect All": "Select All") </div> </HeaderTemplate> <ItemTemplate> <div @onclick="@(e=> OnCheckboxDivClick(e, @context.ProductID))"> <input type="checkbox" id="@("checkbox"+context.ProductID)" class="k-checkbox" checked="@GetChecked(context.ProductID)"/> @context.ProductName </div> </ItemTemplate> </TelerikMultiSelect> @for(int i=0; i <SelectedProductIDs.Count();i++) { <p>The id is @SelectedProductIDs[i]</p> } <style> .single-tag-mode ul.k-reset { float: left; } .single-tag-mode ul.k-reset li.k-button { display: none; } .single-tag-mode ul.k-reset:before { content: "Selected items: @SelectedProductIDs.Count"; display: inline-block; line-height: 1.8em; padding: 0 7px; vertical-align: bottom; border: 1px solid rgba(0, 0, 0, 0.08); background: #f5f5f5 linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.02)); } </style> @code { bool AllChecked=false; bool GetChecked(int id) { return SelectedProductIDs.Contains(id); } public void OnCheckboxDivClick(object ee, int id) { if (id==0) { SelectedProductIDs=new List<int>(); AllChecked=!AllChecked; MakeAllCheckboxChecked(AllChecked); } else { AllChecked=false; SelectedProductIDs.Add(id); } } void MakeAllCheckboxChecked(bool allchecked) { if (allchecked) { var temp=new List<int>(); for (int i=0; i <Products.Count(); i++) { temp.Add(Products[i].ProductID); } SelectedProductIDs=new List<int>(temp); } } List<Product> Products=new List<Product>(); List<int> SelectedProductIDs=new List<int>(); protected override async Task OnInitializedAsync() { for (int i=1; i <=10; i++) { Products.Add(new Product() { ProductID=i, ProductName="ProductName " + i }); } await base.OnInitializedAsync(); } public class Product { public int ProductID { get; set; } public string ProductName { get; set; } } } Please find the below images I have attached which might make my requirements more concise to you. Image noneSelected is the requirement when none of the elements are selected. Image fourSelected is the requirement when any of the options of the elements are selected. Image allSelected is the requirement when all of the elements are selected.

### Response

**Marin Bratanov** commented on 02 Feb 2022

It seems like you also need this feature: [https://feedback.telerik.com/blazor/1529439-refresh-popup-method.](https://feedback.telerik.com/blazor/1529439-refresh-popup-method.) I've added your Vote for it for you. I can suggest you consider building the whole UX from scratch with something like a grid and an animation container to have full control over all aspects. Something like this component would provide.
