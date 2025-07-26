# Grid Column Filter value?

## Question

**con** asked on 23 Jun 2020

Hi, How do I know what Filter user set for given Column ? I see examples of how to set Filter using State property but don't see anything of how to read Filter value. Please advise

## Answer

**Marin Bratanov** answered on 23 Jun 2020

Hello, The following section of the documentation explains how you can do that: Get and Override User Action That Changes The Grid - you can capture when filters change and get them from the grid state. The alternative is to implement the grid operations yourself as explained here: Manual DataSource Operations - the OnRead event will give you the grid request so you can extract the information you want from it. Regards, Marin Bratanov
