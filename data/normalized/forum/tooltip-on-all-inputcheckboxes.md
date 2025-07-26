# Tooltip on ALL Inputcheckboxes

## Question

**Jon** asked on 08 May 2020

Hi How can I apply the same ToolTip on all InputCheckBox controls <TelerikTooltip TargetSelector=" ?????? " Position="@TooltipPosition.Right" ShowOn="@TooltipShowEvent.Hover" Id="position-tooltip"> </TelerikTooltip> <td><InputCheckbox id="cust" class="form-control" style="width: 50px;" @bind-Value="Customer.Active" /> </td> thx in advance

## Answer

**Marin Bratanov** answered on 11 May 2020

Hi Jonathan, The TargetSelector is a CSS selector, so that's how you can target all such components with a standard selector. Here's a sample I made for you that will target all checkboxes: @using System.ComponentModel.DataAnnotations;

<EditForm Model="@exampleModel" OnValidSubmit="HandleValidSubmit">
<DataAnnotationsValidator />
<ValidationSummary />

<table>
<tr>
<td>
<InputCheckbox id="cust1" class="form-control" style="width: 50px;" @bind-Value="@exampleModel.Field1" title="first" />
</td>
<td>
<InputCheckbox id="cust2" class="form-control" style="width: 50px;" @bind-Value="@exampleModel.Field2" title="second" />
</td>
<td>
<InputCheckbox id="cust3" class="form-control" style="width: 50px;" @bind-Value="@exampleModel.Field3" title="third" />
</td>
<td>
<InputCheckbox id="cust4" class="form-control" style="width: 50px;" @bind-Value="@exampleModel.Field4" title="fourth" />
</td>
</tr>
</table>
<button type="submit">Submit</button>
</EditForm>

<TelerikTooltip TargetSelector=" input[type='checkbox'] " />

@code { private ExampleModel exampleModel=new ExampleModel(); private void HandleValidSubmit ( ) {
Console.WriteLine( "OnValidSubmit" );
} public class ExampleModel { public bool Field1 { get; set; } public bool Field2 { get; set; } public bool Field3 { get; set; } public bool Field4 { get; set; }
}
} Regards, Marin Bratanov

### Response

**Jonathan** answered on 11 May 2020

How to I make the tooltip - "Check for YES / Uncheck for NO" ? thx again!

### Response

**Marin Bratanov** answered on 11 May 2020

Hello Jonathan, Have you tried setting the title attribute of the checkboxes themselves? The Telerik Tooltip takes that as its content by default: [https://docs.telerik.com/blazor-ui/components/tooltip/overview.](https://docs.telerik.com/blazor-ui/components/tooltip/overview.) Alternatively, you can set the desired content in the tooltip template. Regards, Marin Bratanov

### Response

**Jonathan** answered on 11 May 2020

thx again!
