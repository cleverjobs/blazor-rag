# Loop through grid rows and hide conditionally

## Question

**JimJim** asked on 17 Apr 2023

Hello all, I am evaluating the Blazor controls for our company, and we are new to Blazor. We are converting from old ASP.NET webforms to Blazor. Since we do use the GridView a lot, I am trying to convert one of our grids to the Telerik grid. Currently, one of the business rules is they want to be able to hide rows based on a checkbox OnValueChanged. I do this on the old grid using JQuery and based on a value in a hidden field I hide the row or not. While playing with the Telerik grid with in-cell editing, I was able to find that hiding a column is easy, but I have not found a way to loop through rows which I assume I cannot since it is client side. OnRowRender will not work because I need this to happen based on the checkbox value. So, basically is there a way to do this using strictly Blazor syntax with functionality from the grid, or will I need to use JQuery again? Thanks for any guidance, Jim

## Answer

**Jim** answered on 24 Apr 2023

I wound up using FilterDescriptors GridState <ProductDto> desiredState=new GridState <ProductDto> ()
{
FilterDescriptors=new List <IFilterDescriptor> ()
{
new CompositeFilterDescriptor(){
FilterDescriptors=new FilterDescriptorCollection()
{
new FilterDescriptor() { Member="ProductId", Operator=FilterOperator.IsGreaterThan, Value=10, MemberType=typeof(int)}
}
}
};

await GridRef.SetStateAsync(desiredState);
