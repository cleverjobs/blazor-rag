# Item per page not shown on pager dropdown.

## Question

**ano** asked on 28 Dec 2023

I have tried the following code on the official page of the Telerik pager <TelerikPager Total="@Games.Count" ButtonCount="5" PageSize=@PageSize Page=@Page PageSizes="@PageSizesList"> </TelerikPager> @{ // take and render the relevant data portion based on the pager info var pageData=Games.Skip((Page - 1 ) * PageSize).Take(PageSize).ToList(); @foreach (Game game in pageData) { <div style="display: inline-block;border: solid;padding: 10px;margin: 10px"> @game.GameName </div> } } @code { public List <int?> PageSizesList { get; set; }=new() { 10, 20, 30 }; public int PageSize { get; set; }=20; public int Page { get; set; }=1; public List <Game> Games { get; set; } protected override void OnInitialized() { Games=new List <Game> (); for (int i=1; i <=20; i++) { Games.Add(new Game() { GameId=i, GameName=$"Game {i}" }); } } public class Game { public int GameId { get; set; } public string GameName { get; set; } } } The output is as follows: Image 1. Output Image 2: Items per page show all options I've configured a PageSize of 20 with PageSizes as {5, 6, 7, 8, 9, 10, 20}, and intentionally excluded null to avoid an "All" option in the items-per-page dropdown. However, when the PageSize matches the total count of data (20 in this instance), the dropdown doesn't automatically select the matching option (20). In the second image, all dropdown options are visible, but the appropriate option (20) isn't auto-selected. What is the solution to this issue?

## Answer

**Radko** answered on 01 Jan 2024

Hi Anoj, What you have described is a known a bug as reported here: A blank value appears in the dropdown when PageSize is not within the predefined PageSizes or equals the TotalCount. The best way to know when it will get resolved is to subscribe to the thread, as this way you will receive notifications in regards to its status. Regards, Radko Progress Telerik
