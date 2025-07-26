# TelerikGridLayout Columnspan does not work with TelerikFloatingLabel

## Question

**Die** asked on 28 Feb 2024

When I use the ColumnSpan property on a floating label, the label itself will grow to the number of columns, but the content of the label will always get the size of the column the floating label is int. Below is the code I've used: @page "/gridLayout" <TelerikGridLayout>
<GridLayoutColumns>
<GridLayoutColumn Width="200" />
<GridLayoutColumn Width="200" />
<GridLayoutColumn Width="200" />
<GridLayoutColumn Width="200" />
</GridLayoutColumns>

<GridLayoutItems>
<GridLayoutItem Column="1" Row="1" ColumnSpan="3">
<TelerikTextBox Title="Filial" />
</GridLayoutItem>
<GridLayoutItem Column="1" Row="2" ColumnSpan="3">
<TelerikFloatingLabel Text="Pessoa">
<TelerikTextBox />
</TelerikFloatingLabel>
</GridLayoutItem>
</GridLayoutItems>
</TelerikGridLayout> This is how it's rendered:

## Answer

**Diego Modolo** answered on 08 Mar 2024

I was able to fix it by adding the following to my site.css file: /* Telerik floating label */ . k-floating-label-container { width: 100 %; }
