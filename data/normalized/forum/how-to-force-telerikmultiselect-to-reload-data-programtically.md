# How to force TelerikMultiSelect to reload data programtically?

## Question

**Joh** asked on 24 Sep 2024

I have a control that has a form on it. That form has a MultiSelect control on it. The Multiselect is populated with records from a DB Table. I have also added a button below the multiselect control that triggers a window control that allows the user to add a new record to that table. When I close the window I would like to refresh the multiselect control without refreshing the whole form that it is part of. How do I go about refreshing only the MultiSelect control? <TelerikMultiSelect @bind-Value="@AppState.Party.SelectedAssocFirmIds" TItem="AssocFirmDDL" Placeholder="Click here for existing firms or add a new one." TValue="int" ValueField="Id" TextField="Name" OnRead=@ReadAssocFirms AdaptiveMode="AdaptiveMode.Auto" Filterable="true" Id="AssocFirms" Width="90%"> </TelerikMultiSelect> <TelerikButton Icon="SvgIcon.Plus" OnClick="@(()=>AssocFirmWindowIsVisible=!AssocFirmWindowIsVisible)"> Add New Firm </TelerikButton> private async Task ReadAssocFirms ( MultiSelectReadEventArgs args ) { try {
DataSourceRequest dsr=CreateDataSourceRequest(); var assocFirms=await AssocFirmServices.GetAssocFirmsOnly(dsr);
args.Data=mapper.Map<List<AssocFirm>, List<AssocFirmDDL>>(assocFirms.AssociatedFirms);
} catch (Exception ex)
{
logger.LogError( $"Error reading Associated firms for DDL.", ex.GetBaseException().Message); throw;
}
}

### Response

**John** commented on 26 Sep 2024

This has been resolved. And should be considered closed.

### Response

**n/a** commented on 04 Mar 2025

What was the solution?

## Answer

**Tsvetomir** answered on 27 Sep 2024

Hello John, Thank you for the update. I'm glad to hear that you've resolved the matter on your own. Now I'm closing the ticket. Regards, Tsvetomir Progress Telerik
