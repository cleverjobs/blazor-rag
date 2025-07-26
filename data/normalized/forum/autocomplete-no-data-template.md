# autocomplete & No Data Template

## Question

**Lou** asked on 21 Mar 2023

Hello. It's possible to hide No Data Template if, when typing, no value are found? THanks

### Response

**Joana** commented on 23 Mar 2023

Hello Louis, If you would like to receive an empty popup, you might simply set empty NoDataTemplate. However, the default behavior is to always open a popup to give the user information what is the filtered data. So, if you do not want to show the popup at all it might lead to a flickering. Below you can find an example REPL and if you uncomment the closing code from the template you will see an alternative to hide the popup. [https://blazorrepl.telerik.com/wHOHGdkV24mUL2pP34](https://blazorrepl.telerik.com/wHOHGdkV24mUL2pP34) Perhaps, there might be another alternative with hiding with css, but would require OnRead handling the filtering so that we are aware when to hide the popup.

## Answer

**Louis** answered on 25 Mar 2023

Hello Joana. THanks for your time. Works! »But as you said it s flickering a bit. I use OnRead and maybe as you said I can manipulate something to hide it w/o flickering. async Task OnReadAutoCompleteOuvertureNomFr(AutoCompleteReadEventArgs args)
{
if (args.Request.Filters.Count> 0) // wait for user filter input
{
Telerik.DataSource.FilterDescriptor filter=args.Request.Filters[0] as Telerik.DataSource.FilterDescriptor;
string userInput=filter.Value.ToString();
args.Data=await OuvertureRisqueActionDataService.ObtenirOuvertureNomAutoCompleteAsync(SafetyStudioSolution.Shared.Constants.cultureNameFr, userInput);
if(args.Data==null)
{
AutoCompleteRefOuvertureNomFr. ??????????
}
}
} Any one have a suggestion? Thank you again Joana
