# Popup no wrong location appears.

## Question

**Kla** asked on 22 Dec 2020

Hi,
I'm doing a test with the blazor but in the combo as I click to appear the list the items appear far from the component. Can you help me with that? Thanks. <div class="col-md-6"> <label class="form-label">Categoria</label>
<TelerikComboBox Data="@_categorias" Filterable="true" FilterOperator="StringFilterOperator.Contains" Placeholder="Selecione a Categoria" @bind-Value="@subcategoria.CodigoGrupo" TextField="Descricao" ValueField="Id" Id="CBCategoria" AllowCustom="false" Width="100%"> </TelerikComboBox></div>

## Answer

**Marin Bratanov** answered on 23 Dec 2020

Hello Klayton, The following section of the documentation treats the most common reasons for such problems: [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#wrong-popup-position.](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#wrong-popup-position.) If it does not help you move forward, I recommend you open a support ticket and send us a simple runnable example that shows the problem. Regards, Marin Bratanov

### Response

**Klayton** answered on 26 Dec 2020

Hi, It worked out following Marin Bratanov's instructions, Thank you very much

### Response

**Dean** answered on 27 Jan 2021

My problem is similar, as I start typing in the combo box, the list of options covers where I am typing so I can't see what I'm typing. I have check the stuff in the link - any other idea? Images attached.

### Response

**Marin Bratanov** answered on 27 Jan 2021

Hi Dean, The article linked above summarizes the known causes for such problems. If it does not help you move forward, I advise that you open a support ticket and send us a simple runnable example of the Telerik problem (remove business logic, actual data, databases and dependencies, just the isolated Telerik component with a few hardoded items of data to showcase the problem). Regards, Marin Bratanov

### Response

**Dean** answered on 02 Feb 2021

Found the issue, thanks.

### Response

**Marin Bratanov** answered on 02 Feb 2021

Hello Dean, Would you mind sharing it with the community, it might help someone else? Regards, Marin Bratanov

### Response

**Dean** answered on 10 Feb 2021

It's covered in the link you sent

### Response

**Marin Bratanov** answered on 10 Feb 2021

Thanks for the update, Dean. Regards, Marin Bratanov

### Response

**Qian** answered on 03 Nov 2022

I found a solution to this. Add the following codes: <style> .k-animation-container{ position:fixed } </style>
