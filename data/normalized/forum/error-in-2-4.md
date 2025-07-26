# Error in 2.4

## Question

**Ric** asked on 19 Nov 2019

Upgraded to the latest and am getting these errors. Project builds and so far seems to function regardless. SeverityCodeDescriptionProjectFileLineSuppression State ErrorCS0234The type or namespace name 'Shared' does not exist in the namespace 'PurchaseRequest' (are you missing an assembly reference?)PurchaseRequestC:\Users\rjd\source\repos\PurchaseRequest\PurchaseRequest\Pages\Index.razor1Active ErrorCS0246The type or namespace name 'MainLayout' could not be found (are you missing a using directive or an assembly reference?)PurchaseRequestC:\Users\rjd\source\repos\PurchaseRequest\PurchaseRequest\Pages\Index.razor1Active ErrorCS0234The type or namespace name 'Shared' does not exist in the namespace 'PurchaseRequest' (are you missing an assembly reference?)PurchaseRequestC:\Users\rjd\source\repos\PurchaseRequest\PurchaseRequest\Pages\Index.razor1Active

## Answer

**Marin Bratanov** answered on 19 Nov 2019

Hi Rick, Can you confirm that you have .NET Core 3.1 Preview 3 installed? This looks like an issue with the builds and I do not see anything related to the Telerik components in these errors. So, you can try running a Clean+Rebuild to see if this helps. If not, try deleting all the bin and obj folders in the project(s) and rebuild them. Regards, Marin Bratanov

### Response

**Rick** answered on 19 Nov 2019

I had done all of that and restarted VS but it was still there. Rebooting machine cleaned it up.
