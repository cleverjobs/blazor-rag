# How to display the "Display(Name="My Name") data annotation with a form field?

## Question

**Jst** asked on 06 Jul 2021

I use data annotations heavily in my view models. I understand that if I let the Telerik form tag I can get the labels to generate and display from my data annotations but I am not auto generating my forms. How do I make use of the Data Annotations with hand crafted forms?

## Answer

**Marin Bratanov** answered on 06 Jul 2021

Hello, The solution is to use a bit of reflection to extract the model metadata that you want to use, you can find similar examples here: [https://stackoverflow.com/questions/7027613/how-to-retrieve-data-annotations-from-code-programmatically](https://stackoverflow.com/questions/7027613/how-to-retrieve-data-annotations-from-code-programmatically) - you can easily make that into an extension method to call from the UI rendering. Regards, Marin Bratanov Progress Telerik
