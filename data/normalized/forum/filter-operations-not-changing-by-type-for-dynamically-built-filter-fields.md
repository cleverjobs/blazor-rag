# Filter Operations Not Changing By Type For Dynamically-Built Filter Fields

## Question

**Bil** asked on 24 May 2023

Our site is building our filter in the following way: <TelerikFilter @ref="@FilterControl" Value="@Value" ValueChanged="@OnValueChanged"> <FilterFields> @foreach (SearchFieldConfiguration searchField in SearchFields)
{ <FilterField Name="@nameof(@searchField.DisplayName)" Type="@(Type.GetType(@searchField.Type))" Label="@searchField.DisplayName" /> } </FilterFields> </TelerikFilter> We want to be able to configure our Search Fields in the database and serialize the DataSourceRequest to handle searching in a separate API. SearchField.Type is a string, examples being "System.Double", "System.String", so that System.Type.GetType(searchField.Type) returns the type we desire. The filter gets built correctly with the search fields in the FilterField field dropdown, but the operations are always string operations (I think the first type in this list is a string). If I select a field that is of type System.Int32 or System.Double, the string operations (contains, etc) remain. Am I missing some refresh action I have to implement?

## Answer

**Bill** answered on 25 May 2023

I figured this one out- @nameof(@searchField.DisplayName) in the Name param always resolves to "DisplayName" and so the control doesn't register the change of filter field selection. If you change to Name="@searchField.DisplayName" or Name="@searchField.Id" then the operators change as expected. Hope this helps a future dev.
