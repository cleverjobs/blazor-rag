# Multiselect readonly

## Question

**Ray** asked on 16 Feb 2022

How can I make a Multiselect readonly? I want to show a list of "chips" and this is very close to what I want: <TelerikMultiSelect Data="@Values" Enabled="true" @bind-Value="@Values" ClearButton="true" AutoClose="false" MinLength="100000" /> But I don't want the user to type anything. I can not set it to disabled because I want to be able to close the chips, so what I want is a readonly possibility. Is this possible to do?

## Answer

**Marin Bratanov** answered on 17 Feb 2022

Hello Raymond, If the component were read-only, then you should not be able to remove selected items. What you can consider is using the ValueChanged event to determine what the user did - whether they tried to add or remove items, so you can update the view-model only when needed. What I would suggest you consider instead, however, is building a custom component for this, so that you don't have the dropdown either - a basic @foreach over the models can let you render the "chips" and a button with a lambda expression can remove them by passing the current item to the handler that will update the view-model. Regards, Marin Bratanov
