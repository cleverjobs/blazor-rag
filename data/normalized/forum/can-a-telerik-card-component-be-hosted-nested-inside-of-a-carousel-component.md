# Can a Telerik Card Component be hosted / nested inside of a Carousel component

## Question

**Bil** asked on 15 Aug 2022

I thought this was going to be an easy enough solution to host a component inside a component but it is proving a little more difficult. In my use case I have several Card components with a data source and template. Those cards sit in a Blazor Component page. I want to host those cards inside of a carousel component. I do not know what to use for the Data property or the template within the Carousel. <TelerikCarousel Data=<CardBlazorComponentPage></CardBlazorComponentPage> Width="400px" Height="200px"> <Template> <div class="item"> idk_what_to put in here</div> </Template> </TelerikCarousel> Would I just put the card logic inside the Template instead of the having its own page. If I did nest the Card code inside of the Carousels Template tag, what would I use for the Carousels Data property?

## Answer

**Tsvetomir** answered on 15 Aug 2022

Hi Bill, By design, the Data attribute of the Card component accepts a collection. Therefore, it could not consume a Razor component directly. One approach is to supply a list of integers that would indicate the number of items shown in the carousel. Check the following REPL: [https://blazorrepl.telerik.com/mmEMbJlM15z9TuEy13](https://blazorrepl.telerik.com/mmEMbJlM15z9TuEy13) Alternatively, you could supply a collection of complex objects that will be used in the card component. The properties of the respective item can be accessed via the context exposed in the Template option of the Carousel component. It would be very helpful if you can share an example of the data that you are currently working with and the CardBlazorComponentPage declaration so that I can look at the big picture and provide suggestions accordingly. Looking forward to your reply. Best regards, Tsvetomir Progress Telerik

### Response

**Bill** answered on 17 Aug 2022

Unfortunately, I can not share any of my data (not even the dev stuff) because of the nature of the data and where I work. I try to replicate my issue in code blocks below, please forgive me. If I posted data, men in suits with handcuffs would come pick me up. I have three Razor component pages all listed in a pages folder in my project: Index.razor MetricsCarousel.razor MetricsCards.razor Index razor is my landing page for the site. The site is a dashboard composed of tiles formatted using the TileLayout component. MetricsCarousel is a component page that will house a Telerik Carousel component. Normally, there is a data property that points to where the data is coming from for the component. There is also a Template property that describes the HTML used for each item in the Carousel. MetrisCards is a component page that also has a data property and template property to describe where the data is coming from and how the HTML will be formatted. We really like the options available to us from your demo page with Cards: Likes and Comments. We are trying to maximize the layout by using both Card components inside a Carousel Component. I do not know what values to use for the data property and template property for the Carousel component if I am to host multiple Card components inside a Carousel component? Here is the closest I can get to the design using your demos: Index.razor @page "/" <TelerikTileLayout Columns="5" ColumnWidth="300px" RowHeight="235px" Reorderable="true" Resizable="true" OnResize="@ItemResize"> <TileLayoutItems> <TileLayoutItem HeaderText="Department Metrics for the month" ColSpan="2"> <Content> <MetricsCarousel> </MetricsCarousel> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> @code {
} MetricsCarousel.razor @page "/MetricsCarousel" <TelerikCarousel Data="@???" Width="512px" Height="384px"> <Template> <div> <MetricsCards> </MetricsCards> </div> </Template> </TelerikCarousel> MetricsCards.razor @page "/MetricsCards" <div class="k-card-deck justify-center"> @foreach (var item in Items)
{ <div> <TelerikCard Width="250px"> <CardHeader> <div> <CardTitle> @item.Title </CardTitle> </div> </CardHeader> <CardSeparator> </CardSeparator> <CardBody> @foreach (var comment in item.Comments)
{ <CardComment Comment="@comment"> </CardComment> } </CardBody> </TelerikCard> </div> } </div> @code {
public List <CardItem> Items { get; set; }

protected override Task OnInitializedAsync()
{
Items=new List <CardItem> ()
{
new CardItem()
{

Comment="Department B had 63,000 new accounts",
Comments=new List <CardCommentModel> ()
},
new CardItem()
{
Comment=Department C had 10 new accounts - needs improvement",
Comments=new List <CardCommentModel> ()
},

new CardItem()
{
Comment=Department d had 1000 new accounts - up from last month",
Comments=new List <CardCommentModel> ()
},

new CardItem()
{
Comment=Department D had 3,500 new accounts - WOW Major improvement",
Comments=new List <CardCommentModel> ()
},
};
return base.OnInitializedAsync();
}
} CardItem.cs using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace TelerikBlazorDemos.Models
{
public class CardItem
{
public string Comment { get; set; }
}
} There is a lot more we would like to do like use the Like and Comment actions and for cards where the score was a major improvement use a Green color and cards that showed negative improvement use a Red color background. Right now I am just trying to get Cards to work inside a Carousel. Can you help?

### Response

**Tsvetomir** commented on 18 Aug 2022

Hi Bill, I completely understand your position regarding sensitive data. Indeed, we do not require any specific data or property names, you can substitute the names and the actual data with dummy text. What is important is the structure of the classes so that we can determine the best way to handle the scenario based on the structure of the classes and the hierarchy of properties. I have investigated the provided code snippets and what I can recommend as a small change is to use the Items collection from the MetricsCards component inside the Data parameter of the Carousel. The MetricsCards should become a MetricsCard so that it handles a single card at a time. Basically, you get rid of the foreach loop and let the Carousel do the data iteration for you. Currently, even if the data was valid, you would render all cards inside a single item of the Carousel. I suspect that you would like to have a single card per carousel item, is that correct? If yes, pass the Items collection to the Data of the Carousel. After that, every single item from the Items collection is accessible via the context of the Template. Pass the context to the MetricsCard component that will be responsible for constructing the card. I hope you find those clarifications helpful. If additional information is needed, do let me know.

### Response

**Bill** commented on 18 Aug 2022

Your answer does make sense. I do not want all the cards to show up as one item on the Carousel. So to repeat just so I understand, remove the Blazor UI Card Component and just use the Card info and Carousel component. I was wanting to use the Card Component inside of the Carousel Component because of the Card Actions with Likes and Comments. Being able to add comments is actually a requirement. Can the same actions (Likes, comments) be added to an item inside the Carousel? That would allow me to keep both requirements of a Carousel and User Comments.

### Response

**Tsvetomir** commented on 22 Aug 2022

Hi Bill, The card component still can be used within the context of the carousel. However, the idea is to use the MetricCard component for a single item from the carousel instead of receiving a list that should be looped through. I have prepared a sample REPL where you can find a more practical example of the idea proposed earlier.
