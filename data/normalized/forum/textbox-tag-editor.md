# Textbox Tag Editor?

## Question

**Tim** asked on 04 Jun 2021

Is there any way to do a textbox tag editor like the one below from this forum (see attached)?

## Answer

**Dimo** answered on 08 Jun 2021

Hello Timothy, The tag selector is a MultiSelect: [https://demos.telerik.com/blazor-ui/multiselect/overview](https://demos.telerik.com/blazor-ui/multiselect/overview) The visible tag list below the MultiSelect can be implemented with a ListView with a Button inside its Template: [https://demos.telerik.com/blazor-ui/listview/templates](https://demos.telerik.com/blazor-ui/listview/templates) Here is a quick and simple POC. @page "/t1522562" @using System.Collections.ObjectModel

<h3>Ticket 1522562 </h3> <TelerikMultiSelect Data="@Countries" @bind-Value="@Values" Filterable="true" Placeholder="type a country" Width="600px"> </TelerikMultiSelect> <TelerikListView Data="@Countries" Class="tag-list"> <Template> <TelerikButton OnClick="(MouseEventArgs args)=> CountryClick(args, context)"> @context </TelerikButton> </Template> </TelerikListView> <style>.tag-list { border: 0; margin-top: 1em;
}.tag-list.k-listview-content { overflow: visible;
}.tag-list.k-button { margin-right: . 4em;
} </style> @code {

private List<string> Values { get; set; }=new List<string>();

private List<string> Countries { get; set; }=new List<string>() { "France", "Germany", "Italy", "Spain", "United Kingdom" };

private async Task CountryClick(MouseEventArgs args, string country)
{ var valuesInternal=new ObservableCollection<string>(Values); var index=valuesInternal.IndexOf(country); if (index> -1 )
{
valuesInternal.RemoveAt(index);
} else {
valuesInternal.Add(country);

}
Values=valuesInternal.ToList<string>();
}
} Regards, Dimo Progress Telerik

### Response

**Timothy J** commented on 08 Jun 2021

Cool! I'll check it out. Thanks!
