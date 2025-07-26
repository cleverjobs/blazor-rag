# Two way binding with OnRead in 3.0

## Question

**RobRob** asked on 20 Jan 2022

I'm trying to programmatically change the value of an existing ComboBox to something that's not in the last OnRead args.Data list. Is there a way for me to achieve this and populate the TextField? The only way I can see is to destroy the control and remake it, triggering the initialization OnRead.

## Answer

**Dimo** answered on 25 Jan 2022

Hello Rob, In UI for Blazor 3.1 (due in early March) we will add a method to reload data when using OnRead. In the meantime, it is possible to do this in two ways: recreate the component, as you have already tried toggle the ValueField of the component - I agree this is not a very ingenious approach, but I am mentioning it in case you find this more convenient for your scenario <TelerikComboBox OnRead="@OnComboRead" ValueField="@ComboValueField" /> @code { string ComboValueField { get; set; }="Id"; async Task RefreshCombo ()
{
ComboValueField="Name"; await Task.Delay( 1 );
ComboValueField="Id";
} async Task OnComboRead(ComboBoxReadEventArgs args)
{ if (ComboValueField=="Id" ) { var result=await MyService.GetItems(args.Request);

args.Data=result.Data;
args.Total=result.Total;
}
}
} Regards, Dimo

### Response

**Rob** commented on 25 Jan 2022

Thanks Dimo, I'll continue migrating the rest to be ready for 3.1 then!
