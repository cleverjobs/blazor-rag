# Nested class TextField

## Question

**RobRob** asked on 04 Sep 2020

This lightly modified ComboBox sample won't show the value of the nested class. Filtering does work, so I think this is a bug? <TelerikComboBox @bind-Value=@SelectedValue Data="@ComboBoxData" Filterable="true" ValueField="ProductId" TextField="ProductName.Description"> <ItemTemplate> <strong>@((context as Product).ProductName.Description) - @(String.Format("{0:C2}", (context as Product).UnitPrice))</strong> </ItemTemplate> </TelerikComboBox> @code { public IEnumerable<Product> ComboBoxData { get; set; } public int SelectedValue { get; set; }=2; protected override void OnInitialized() { List<Product> products=new List<Product>(); for (int i=1; i <10; i++) { products.Add(new Product() { ProductId=i, ProductName=new ProductName {Description=$"{i} Product {i}"}, UnitPrice=(decimal)(i * 3.14) }); } ComboBoxData=products; base.OnInitialized(); } public class Product { public int ProductId { get; set; } public ProductName ProductName { get; set; } public decimal UnitPrice { get; set; } } public class ProductName { public string Description { get; set; } } }

## Answer

**Marin Bratanov** answered on 04 Sep 2020

Hello Rob, You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1464290-combobox-support-nested-complex-models.](https://feedback.telerik.com/blazor/1464290-combobox-support-nested-complex-models.) I've added your Vote for it on your behalf in order to raise its priority. For the time being, my best suggestion is to flatten the model or prepare a separate model for the combo box data. What you are seeing in the textbox input is the result of the accessor of the TextField - it cannot pull from the nested model and so you get a string representation of what it does get - the class name of Product. The filtering relies on the DataSource package code where there are some provisions for that already, but this is not implemented in the combo box component itself yet. Regards, Marin Bratanov
