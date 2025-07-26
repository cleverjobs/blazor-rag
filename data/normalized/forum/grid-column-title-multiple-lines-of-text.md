# Grid Column Title Multiple Lines Of Text

## Question

**Geo** asked on 04 Nov 2020

I want to display multiple lines in the grid Title. I've tried <br /> and \n. They show up as literal characters. I've modified the css for grid header height to be set to auto and the long text wraps but not where I want it to wrap. Here is an example: This is what I want it to look like: Labor
& Burden Cost Type 1234 Here is how it shows up: Labor & Burden Cost Type 1234 How do I force the wrapping of the text where I want it?

## Answer

**Marin Bratanov** answered on 05 Nov 2020

Hello George, Blazor encodes HTML from strings when rendering, and that applies to our components too. This is why you can't use HTML in such literals. What you can do is to use the HeaderTemplate of the column which lets you define your content as desired: [https://docs.telerik.com/blazor-ui/components/grid/templates/column-header](https://docs.telerik.com/blazor-ui/components/grid/templates/column-header) Regards, Marin Bratanov
