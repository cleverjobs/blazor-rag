# Grdi support of OData V4.01 and the "in" or "containedin" functionality?

## Question

**Jst** asked on 08 Jun 2021

Does the GridReadEventArgs support some sort of in functionality? I am trying to programmatically use several multiselect lists to create the initial query for loading data into a grid via an OData datasource. The "query" created is close but the fieldname is surrounded by single quotes so the query does not work This is what is created filter=(contains( 'abc,DEF', 'MyColName' )) but this is the proper syntax filter=(contains( 'abc,DEF', MyColName)) Is there anyway short of manipulating the resulting query string to remove the single quotes from around 'MyColName'? Or IsContainedIn now supported in the latest version of the Blazor UI library?

## Answer

**Nadezhda Tacheva** answered on 11 Jun 2021

Hi John, You can manipulate the resulting query string from ToODataString() of the DataSourceRequest to achieve the desired scenario. For example: var result=args.DataSourceRequest.ToODataString()
result="$filter=(...)" In terms of the IsContainedIn operator, it is generally available in Blazor, however, as "in" operator is not supported by earlier than OData v4.01, to be able to cover all possible scenarios (for example some applications might be using older versions), the IsContainedIn operator is currently translated to Contains. I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva Progress Telerik
