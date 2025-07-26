# Weblink not clickable

## Question

**Dav** asked on 30 Jan 2025

Code <FormItem Field="@nameof(NewRecordClaim.EvidenceLink)" Id="EvId" LabelText="Evidence Link" Enabled="false"> <Template> <label for="EvidenceLink" class="k-label k-form-label"> Link: </label> <div class="k-form-field-wrap"> <a target="_blank" href="@MyModel.EvidenceLink"> View evidence at @MyModel.EvidenceLink </a> </div> </Template> </FormItem> MyModel.EvidenceLink is for example [https://athsvic.resultshub.com.au](https://athsvic.resultshub.com.au) View evidence at [https://athsvic.resultshub.com.au](https://athsvic.resultshub.com.au) <-- Should get this Get this (unclickable): Link: View evidence at [https://athsvic.resultshub.com.au](https://athsvic.resultshub.com.au)

## Answer

**Anislav** answered on 08 Mar 2025

Hi David, The issue occurs because the Enabled property is set to false in your FormItem, which prevents the link from being clickable. To resolve the issue, remove the Enabled property or set it to true like this: <FormItem Field="@nameof(NewRecordClaim.EvidenceLink)" Id="EvId" LabelText="Evidence Link" Enabled="true"> <Template> <label for="EvidenceLink" class="k-label k-form-label"> Link: </label> <div class="k-form-field-wrap"> <a target="_blank" href="@MyModel.EvidenceLink"> View evidence at @MyModel.EvidenceLink </a> </div> </Template> </FormItem> I’ve also created a REPL page where the issue is fixed: [https://blazorrepl.telerik.com/wTknasbB010K5tDJ27.](https://blazorrepl.telerik.com/wTknasbB010K5tDJ27.) Regards, Anislav Atanasov

### Response

**Anislav** commented on 24 Mar 2025

David, did the suggested solution resolve your issue?

### Response

**David** commented on 03 Apr 2025

Yes thanks!
