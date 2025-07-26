# Disable Enter Key in Grid Inline Edit

## Question

**Kin** asked on 29 Jul 2022

Hello, How can i disable default Enter Key behaviour in Inline Grid Edit? I need to place an TextArea component inside a inline edit row to let user put longer text description in one of the columns. When i try to go to a new line inside TextArea component, clicking enter key is triggering save for the whole inline edit row, making use of TextArea impossible. Could you help me find a solution for this problem? Kind regards, Kinga

## Answer

**Dimo** answered on 02 Aug 2022

Hello Kinga, I assume you have a column EditorTemplate. Wrap the TextArea with a <div> that captures key events and prevents their propagation: <GridColumn Field="@nameof(Product.Description)" Title="Product Description"> <EditorTemplate> @{
var p=context as Product;
} <div @onkeydown:stopPropagation> <TelerikTextArea @bind-Value="@p.Description" /> </div> </EditorTemplate> </GridColumn> Regards, Dimo Progress Telerik

### Response

**Kinga** commented on 02 Aug 2022

Thank you, this is exactly what i needed Regards, Kinga
