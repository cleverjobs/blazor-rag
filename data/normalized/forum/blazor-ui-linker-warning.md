# Blazor UI linker warning

## Question

**Way** asked on 14 Oct 2020

I am getting a linker warning: SeverityCodeDescriptionProjectFileLineSuppression State WarningTelerik.DataSource.Extensions.QueryableExtensions.CallQueryableMethod(IQueryable,String,LambdaExpression): Could not resolve dependency type 'System.Linq.Queryable' specified in a `PreserveDependency` attributeBlazor Wasm Kendo 2.ServerILLink0 Error is from the Server project. Blazor Webassembly Hosted app. VS Version 16.8.0 Preview 4.0 Net5 Version 5.0.100-rc.2.20479.15 Blazor UI Version 2.17.0

## Answer

**Marin Bratanov** answered on 15 Oct 2020

Hello Wayne, While .NET 5 is not yet supported officially, we are working towards compatibility with it. We have not, however, encountered such an error. Could you send us a simple project that showcases the issue so we can have a look? Regards, Marin Bratanov

### Response

**Wayne Hiller** answered on 15 Oct 2020

I just noticed I only get the warning when doing a Publish (folder). This was in the warning list too. SeverityCodeDescriptionProjectFileLineSuppression State WarningTelerik.DataSource.SortDescriptorCollectionExpressionBuilder.Sort(): 'PreserveDependencyAttribute' is deprecated. Use 'DynamicDependencyAttribute' instead.Blazor Wasm Kendo 2.ServerILLink0

### Response

**Marin Bratanov** answered on 15 Oct 2020

Thank you for the clarification, Wayne. The publish warnings from the linker are on our to-do list, yet they don't seem to break anything. Do things work fine for you? Our 2.17.0 release should work with .net 5 even if it is not supported yet. Regards, Marin Bratanov

### Response

**Wayne Hiller** answered on 15 Oct 2020

Yes everything seems to work fine.

### Response

**Marin Bratanov** answered on 15 Oct 2020

Thank you for confirming this. If you do find other issues, let us know. By the way, you may find useful the following two KB articles we already have related to .net 5 features: CSS Isolation feature and nested components WebAssembly Server Pre-rendering Regards, Marin Bratanov

### Response

**Wayne Hiller** answered on 15 Oct 2020

Thank Marin, I will check them out. Great product by the way. I now use Kendo for MVC, Kendo for jQuery, Kendo for Vue and Telerik UI for Blazor :)

### Response

**Marin Bratanov** answered on 15 Oct 2020

Thank you, Wayne, I will make sure the teams sees your post :) I'm happy we're helpful in your development :) Regards, Marin Bratanov
