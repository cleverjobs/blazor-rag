# TelerikGrid filtering problem

## Question

**Ann** asked on 04 Mar 2021

I use TelerikGrid with big data. Everything works fine except filtering.When I'm trying filter grid by name of customers, grid freezes. If I write text in filter slowly, grid filtering works fine, but when writing fast,filtering works after every change and that block my grid and it's broke. How can I prevent grid filtering after every change in string filter?

## Answer

**Nadezhda Tacheva** answered on 05 Mar 2021

Hello Anna, Indeed, when dealing with large portions of data filtering on every keystroke may result in slowing down the application performance. Since the FilterRow mode uses filter-as you-type method as per design, there are a couple of approaches you may try: You can use the FilterMenu mode as it fires filtering only when the user presses a button (the FilterMenu can be simplified to contain only one filter option) Implement debouncing in the OnRead Implement your own filtering More details as well as examples for the above listed approaches you can find in this knowledge base article for Debouncing Grid data source operations. In the meantime, we have an opened feature request for Adding Debounce property for grid filtering in our public
