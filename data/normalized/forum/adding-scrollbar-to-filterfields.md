# Adding scrollbar to FilterFields

## Question

**Joh** asked on 10 Aug 2022

My app has a long list of possible fields to filter on. The dropdown box for the fields exceed the height of the page so a scrollbar would be nice. Can you point out the class styling that needs to be updated? I just added arbitrary number of fields to the Filter demo. <TelerikFilter Value="@Value" ValueChanged="@OnValueChanged"> <FilterFields> <FilterField Name="@nameof(OrderDetailDto.OrderId)" Type="typeof(int)" Label="Id" /> <FilterField Name="@nameof(OrderDetailDto.Quantity)" Type="typeof(short)" /> <FilterField Name="@nameof(OrderDetailDto.OrderFreight)" Type="@typeof(decimal)" Label="Freight" /> <FilterField Name="@nameof(OrderDetailDto.OrderShipCountry)" Type="typeof(string)" Label="Country" /> <FilterField Name="@nameof(OrderDetailDto.OrderShipName)" Type="typeof(string)" Label="Ship to" /> <FilterField Name="@nameof(OrderDetailDto.OrderShipAddress)" Type="typeof(string)" Label="Ship Address" /> @for (int i=0; i <25; i++) { <FilterField Name="@i.ToString()" Type="typeof(string)" Label="@i.ToString()" /> } </FilterFields> </TelerikFilter>

## Answer

**Dimo** answered on 11 Aug 2022

Hello John, (Answer replaced due to misunderstanding) You can apply a max-height style to the dropdown container. Note that the selector will target any dropdowns on the page, so I recommend putting the CSS rule in a specific Razor file, or using another technique to make it work only when necessary. ( Scoped styles in.razor.css files won't work, because popups are rendered in the application root. ) .k-animation-container> div { max-height: 200px;
} Regards, Dimo

### Response

**John** commented on 11 Aug 2022

Thanks for your response. I tried and it didn't help. The dropdown list didn't seem to inherit the scrollable-filter style. See [https://blazorrepl.telerik.com/GcECFFlx54cBXdnH50](https://blazorrepl.telerik.com/GcECFFlx54cBXdnH50)

### Response

**John** commented on 11 Aug 2022

Thanks that worked.
