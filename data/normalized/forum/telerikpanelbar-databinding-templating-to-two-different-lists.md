# TelerikPanelBar Databinding/Templating to two different Lists

## Question

**Dom** asked on 21 Sep 2022

Hi. I want to use the TelerikPanelBar with two different Datasources. For the Header, I have a List "Articles" and for the Content I have an object "ArticleDetails", that will be loaded "lazy" if someone opens the accordion. I want to use also the HeaderTemplate and ContentTemplate Feature. The Samples show only PanelBarItem within a list of PanelBarItems, but I need a total different Object in the Content Area. The Idea is to load a list of Articles, and then when a user clicks on a panel the Details of the Article will be loaded and displayed. Thanks and Regards Dominik

## Answer

**Dominik** answered on 21 Sep 2022

I think, I must use an extra object to hold header and Content information. private class PanelBarItem
{
public int Id { get; set; }
public string Season { get; set; }=null!;
public string Name { get; set; }=null!;
public List <ArticleDetailsDto> ArticleDetails { get; set; }=new List <ArticleDetailsDto> ();
}
