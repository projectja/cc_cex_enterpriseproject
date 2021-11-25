let timer, timeoutVal = 1000;
var current_page = 1;
var page_limit = 10;

$('#hidden-spinner').hide();


function get_list_url(page, query) {
   url = window.location.pathname
   url += `api/list?page=${page}`;

   if (query){
      query = "&" + query
      url += query
   }

   return url
}

function putTableData(data) {
   let row;
   $("#table_body").html("");
   tbody = $("#table_body")

   if (data['results'].length > 0){
      $.each(data['results'], function (a, b){
         row = "<tr data-val="+b.id+"> <td>" + b.name + "</td>" +
               "<td>" + b.sector_actividad + "</td>" +
               "<td>" + b.direccion_actividad + "</td>" +
               "<td>" + b.export_destino + "</td>" +
               "<td>" + b.empleados_fijos + "</td>" +
               "<td>" + b.volumen_facturacion + "</td>" +
               "<td>" + b.export_frecuencia + "</td>"
         tbody.append(row);

      });
   } else {
      $("#table_body").html("No results found.");
   }

   
   pagination = create_pagination_control(data)
   $(".pagination-box").html("")
   $(".pagination-box").append(pagination)

}

function get_datatable (url) {
   $("#table_body").html("");
   $('#hidden-spinner').show();
   
   $.ajax({
      method: "GET",
      url: url,
      success: function(data){
         console.log(data)
         $('#hidden-spinner').hide();
         current_page = parseInt(data.links.current)
         putTableData(data);

         $("#result-count span").html(data.count)
         
         if (data.links.current == null){
            $("#page-count span").html("1")
         } else {
            $("#page-count span").html(data.links.current)
         }
      },
      error: function(response){
         console.log(response)
      }
   })
}

function create_pagination_control(data){
   previous_url = data.links.previous;
   next_url = data.links.next;
   page_links = data.page_links.page_links;


   ul = '<ul class="pagination" style="margin: 5px 0 10px 0">'

   if (previous_url){
      li = `<li>
               <button  class="page-link" data-url="${previous_url}" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
               </button>
            </li>`;
   } else {
      li = `<li class="page-item disabled">
               <button  class="page-link" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
               </button>
            </li>`;
   }
   ul += li;

   $.each(page_links, function (id, page){
      if (page.is_break) {
         li2 = `<li class="disabled">
                  <button  class="page-link"><span aria-hidden="true">&hellip;</span></button>
               </li>`
      } else {
         if (page.is_active ){
            li2 = `<li class="page-item active">
                     <button  class="page-link" id="button-${id}" data-url="${page.url}">${page.number}</button>
                  </li>`
         } else {
            li2 = `<li>
                     <button class="page-link" id="button-${id}" data-url="${page.url}">${page.number}</button>
                  </li>`
         }
      }
      ul += li2;
   });

   if (next_url) {
      li3 = `<li>
               <button class="page-link" data-url="${next_url}" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
               </button>
            </li>`
   } else {
      li3 = `<li class="page-item disabled">
               <button class="page-link" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
               </button>
            </li>`
   }
   ul += li3;
   ul += `</ul>`

   return ul
}

function create_card_info(data){
   // Create a card where enterprise
   // info goes.
   $("#ModalBody").html("")

   // div with card class.
   card = document.createElement('div')
   card.classList.add("card", "detalle-empresa")

   // add card-header with h3 for title.
   header = document.createElement('div')
   header.classList.add("card-header")

   h3 = document.createElement('h3')
   h3.classList.add("card-title")
   h3.innerHTML = "Detalle"

   header.appendChild(h3)
   card.appendChild(header)

   // add card-body
   card_body = document.createElement('div')
   card_body.classList.add("card-body")

   div1 = document.createElement("div")
   div1.classList.add("col-12", "order-1", "order-md-2")

   title = document.createElement("h3")
   title.classList.add("text-primary")
   title.innerHTML = "data.nombre"

   p = document.createElement("p")
   p.classList.add("text-muted")
   p.innerHTML = "Raw denim you probably haven't heard of them jean shorts Austin. Nesciunt tofu stumptown aliqua butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terr."

   br = document.createElement("br")

   div2 = document.createElement("div")
   div2.classList.add("text-muted")

   p2 = document.createElement("p")
   p2.classList.add("text-sm")
   p2.innerHTML = "Poblacion"
   
   b1 = document.createElement("b")
   b1.classList.add("d-block")
   b1.innerHTML = "data.poblacion.nombre"

   p3 = document.createElement("p")
   p3.classList.add("d-block")
   p3.innerHTML = "Partidas"

   b2 = document.createElement("b")
   b2.classList.add("d-block")
   b2.innerHTML = "data.partidas"

   h5 = document.createElement("h5")
   h5.classList.add("mt-5", "text-muted")
   h5.innerHTML = "Project files"

   ul = document.createElement("ul")
   ul.classList.add("list-unstyled")

   li1 = document.createElement("li")
   a1 = document.createElement("a")
   a1.href = "#"
   a1.classList.add("btn-link", "text-secondary")
   a1.innerHTML = "Functional-requirements.docx"

   li1.appendChild(a1)

   li2 = document.createElement("li")
   a2 = document.createElement("a")
   a2.href = "#"
   a2.classList.add("btn-link", "text-secondary")
   a2.innerHTML = "UAT.pdf"

   li2.appendChild(a2)

   li3 = document.createElement("li")
   a3 = document.createElement("a")
   a3.href = "#"
   a3.classList.add("btn-link", "text-secondary")
   a3.innerHTML = "Email-from-flatbal.mln"

   li3.appendChild(a3)

   li4 = document.createElement("li")
   a4 = document.createElement("a")
   a4.href = "#"
   a4.classList.add("btn-link", "text-secondary")
   a4.innerHTML = "Logo.png"

   li4.appendChild(a4)

   li5 = document.createElement("li")
   a5 = document.createElement("a")
   a5.href = "#"
   a5.classList.add("btn-link", "text-secondary")
   a5.innerHTML = "Contract-10_12_2014.docx"

   li5.appendChild(a5)

   ul.appendChild(li1)
   ul.appendChild(li2)
   ul.appendChild(li3)
   ul.appendChild(li4)
   ul.appendChild(li5)

   p3.appendChild(b2)
   p2.appendChild(b1)
   div2.appendChild(p2)
   div2.appendChild(p3)

   div1.appendChild(title)
   div1.appendChild(p)
   div1.appendChild(br)
   div1.appendChild(div2)
   div1.appendChild(h5)

   div1.appendChild(ul)

   card.appendChild(div1)

   card_detalle = document.getElementById("ModalBody")
   card_detalle.appendChild(card)

   return card_detalle

}

$(document).on("click", ".page-link", function (e) {
   e.preventDefault();
   let url = $(this).attr("data-url");

   $('body,html').animate({
      scrollTop: 0
   }, 600);

   get_datatable(url);

})

$('.select2').select2({
   theme: 'bootstrap4',
   language: 'es',
   placeholder: "Seleccione una Opcion",
}).select2('data', null)

$('#EmpresaList tbody').on('click', 'tr', function () {
   // console.log($(this).attr('data-val'))
   card_detail = create_card_info();

   $('#myModal').modal('show')
   $('#ModalBody').append(card_detail)
   
});

$("#id_query" ).on("keypress",function() {
   window.clearTimeout(timer);
   
   $("#table_body").html("");
   $('#hidden-spinner').show();
});
 
$("#id_query" ).on("keyup",function() {
window.clearTimeout(timer);
timer = window.setTimeout(() => {
   var form_data = $("#FilterForm").serialize();
   $('#hidden-spinner').hide();
   get_datatable(get_list_url(1, form_data))
}, timeoutVal);

});

$("#FilterForm input, select").change(function (e){
   form_data = $("#FilterForm").serialize();
   get_datatable(get_list_url(1, form_data))

});

$(".clear-filters").on("click", function(e){
   $("#FilterForm").trigger("reset");
   get_datatable(get_list_url(1));

});

// function removeItem(id){
//    var multi_select_tags = $(".tag-selected");
//    var category_checkbox_list = $(".item-filter")

//    var selected_item = multi_select_tags.find('[data-val="'+ id +'"]');
//    var item = category_checkbox_list.find('[id="' + id +'"]');
//    selected_item.remove();

//    $.each(item.find("option:selected"), function () {
//       // countries.push($(this).val());
//       $(this).prop('selected', false);
//       $(this).val(null).trigger("change");
      
//    });

   
// }


// $(document).ready(function() {
//    var filter_childs = $("#FilterForm");

//    filter_childs.find(".item-filter").change( function(e){
//       var item = $(this);
//       var inputElem = item.find("select, input");
//       var itemLabel = item.find("label")
//       var selectedTag = $(".tag-selected");
      

//       selectedTag.append(
//          '<span class="badge rounded-pill bg-secondary" data-val="'+ inputElem.attr('id') +'" >'+ itemLabel.text() +''+
//             '<button type="button" class="close" aria-label="Close" onclick="removeItem($(this).parent().attr(\'data-val\'));" >'+
//                '<span aria-hidden="true">&times;</span>'+
//             '</button>'+
//          '</span>'
//       );


//       // selected_items = fetch_selected_categories()
      
//       // if (selected_items.length > 0) {
//       //    $.ajax({
//       //       url: window.location.href,
//       //       type: 'POST',
//       //       data: JSON.stringify({ 
//       //          selected_items,
//       //       }),
//       //       success: function(response) {
//       //          console.log(response.data)
//       //       }
//       //    });
//       // }
//    })

// });

get_datatable(get_list_url(current_page));
