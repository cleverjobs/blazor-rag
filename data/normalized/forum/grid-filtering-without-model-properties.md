# Grid filtering without model properties

## Question

**Joh** asked on 12 Jun 2024

Hi, I have a Grid component that is used for editing data in an arbitrary database table. The type of the grid is a class that doesn't have properties for each column, but rather simulates columns and row data based on the selected database table structure. The purpose of this is to enable the user to edit a certain database table without the need to define the exact data structure in the web application. This works fine when displaying data and editing data. However, I need to implement filtering and things start to get tricky. I have a snippet that simplifies the issue: [https://blazorrepl.telerik.com/weYKFcvq2749nY9L57](https://blazorrepl.telerik.com/weYKFcvq2749nY9L57) Before trying to implement filtering, I had no Field attribute on my GridColumns and that worked fine. But when adding the FilterMode attribute to the TelerikGrid component the filter row isn't rendered at all (also not when using FilterCellTemplate). I've read other forum posts about the necessity of the Field attribute. When I add the Field attribute, the filter row is rendered but I get an exception stating "Value cannot be null. (Parameter 'nullableType')" with this stack trace: at System.ArgumentNullException.Throw(String paramName) at System.Nullable.GetUnderlyingType(Type nullableType) at Telerik.Blazor.Common.Filter.FilterOperatorFactory.GetColumnDefaultFilterOperator(Type propType) Is the component using reflection to determine the Type of the field? Or can I somehow tell the component dynamically what type to use, in the same way I can return the title or cell content dynamically? I tried to use the filter template but I get stuck on the Field problem.

## Answer

**Nadezhda Tacheva** answered on 17 Jun 2024

Hi Johannes, In the provided example, I see that you are passing a list of the TestModel to the Grid and you are generating the columns based on the fields in that model. The issue in this case is that the Field value for the third GridColumn instance is "Text" while the actual field name is "Description". You may adjust that to ensure you are passing the correct Field to the column: [https://blazorrepl.telerik.com/cykKbVbO48UX2RQK09.](https://blazorrepl.telerik.com/cykKbVbO48UX2RQK09.) If you have a model as in the provided example, you may also consider the AutoGenerateColumns feature of the Grid. In this case, the Grid will extract the column information from the fields in the model. Apart from that, you mentioned that you want to use the Grid for editing of an arbitrary database table. If you don't have a model, you may consider binding the Grid to dynamic objects as shown in this article: Bind Grid to Expando Object. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Johannes** commented on 19 Jun 2024

Hi Nadezhda and thanks for your reply! It was on purpose that the field value Text resolves to Description, that was only to illustrate that the class doesn't match the model. But yes, it is correct that I in this case don't have a model to rely on. I hadn't thought about the ExpandoObject in this case, and when reading through the documentation again I realize that using a dictionary fits my needs better and now the code doesn't break when enabling filtering. However, the built-in filtering functionality doesn't seem to work when using a dictionary as model. Should this work or do I have to implement the filtering myself with the OnRead event and/or filtering template?

### Response

**Nadezhda Tacheva** commented on 24 Jun 2024

Hi Johannes, I am glad that my suggestion was useful. Whether the built-in filtering will work depends on how your data is organized and provided to the Grid. The Grid provides built-in filtering for strings and value types. So, if you manage to organize your data so that the columns use simple strings or value types as per the first example here, the built-in filtering will work. However, if you work with nullable data or if you have a more complex structure as in the example here, the Grid cannot perform the filtering on its own and you will need to handle that.
