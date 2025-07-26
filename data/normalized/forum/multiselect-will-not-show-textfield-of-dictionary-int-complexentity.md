# MultiSelect will not show TextField of Dictionary<int, ComplexEntity>

## Question

**Zac** asked on 28 Jun 2023

I have a MultiSelect bound to a Dictionary<int, SerialNumberEntry> SNEList <TelerikMultiSelect Data="SNEList" Value="@SelectedSerialNumberEntryIds" ValueExpression="@(()=> SelectedSerialNumberEntryIds)" ValueChanged="@((List<int> newValues)=> SelectSerialNumberEntryChanged(newValues))" AutoClose="false" Placeholder="Select Serial Numbers" ValueField="Key" TextField="Value.SerialNumber" @ref="SerialNumberMultiSelect"> <HeaderTemplate> <div class="select-all-item"> <TelerikCheckBox TValue="bool" Value="@IsAllSerialNumbersSelected()" ValueChanged="@( (bool v)=> ToggleSelectAllSerialNumbers(v) )" Id="ms-select-all-checkbox"> </TelerikCheckBox> <label for="ms-select-all-checkbox"> &nbsp; Select All </label> </div> </HeaderTemplate> <ItemTemplate> <input type="checkbox" id="@( " cb " + context.Key )" class="k-checkbox k-rounded-md k-checkbox-md" checked="@GetChecked(context.Value)"> @context.Value.SerialNumber </ItemTemplate> </TelerikMultiSelect> and when I select an entry, it displays the "ToString()" result of the KeyValuePair<int, SerialNumberEntry> Why does TextField="SerialNumber" work if it's a List<SerialNumberEntry> but it's ignoring the TextField="Value.SerialNumber" when it is a Dictionary<int, SerialNumberEntry>? Can it not bind to child properties? There's no template that I can find to override this behavior.

## Answer

**Yanislav** answered on 03 Jul 2023

Hello Zachary, At present, there is no template that allows modification of the MultiSelect tags. However, we have a feature request in our
