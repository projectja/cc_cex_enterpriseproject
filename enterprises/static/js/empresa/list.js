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

function create_detail_url(detail_url){
   url = window.location.origin
   url += `${detail_url}`
   return url
}

function putTableData(data) {
   let row;
   $("#table_body").html("");
   tbody = $("#table_body")
   var url = 'https://open.spotify.com/genre/fresh_finds-page'
   if (data['results'].length > 0){
      $.each(data['results'], function (a, b){
         row = "<tr id="+b.id+"><td style='display:none;'>" + b.logo + "</td>" +
               "<td>" + b.name + "</td>" +
               "<td>" + b.sector_actividad + "</td>" +
               "<td>" + b.direccion_actividad + "</td>" +
               "<td>" + b.export_destino + "</td>" +
               "<td style='display:none;'>" + b.obj_absolute_url + "</td>" 
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
   logo_url = data.childNodes[0].innerText
   empresa_name = data.childNodes[1].innerText
   sector_actividad = data.childNodes[2].innerText
   ubicacion = data.childNodes[3].innerText
   pais_operacion = data.childNodes[4].innerText
   numero_empleados = data.childNodes[5].innerText
   volumen_facturacion = data.childNodes[6].innerText
   frecuencia_exportacion = data.childNodes[7].innerText
   obj_absolute_url = data.childNodes[8].innerText

   list_country_op = pais_operacion.split(',')

   
   $("#ModalBody").html("")
   modal_header = document.getElementById('exampleModalLabel')
   modal_header.innerHTML= "Detalles"

   div1 = document.createElement("div")
   div1.classList.add("col-12", "order-1", "order-md-2")

   row = document.createElement("div")
   row.setAttribute("class", "row")
   div1.appendChild(row)
   
   logo_col_div = document.createElement("div")
   logo_col_div.setAttribute("class", "col-md-4")
   row.appendChild(logo_col_div)

   logo = document.createElement("img")
   logo.classList.add("img-fluid", "rounded-circle", "mb-4")
   logo.setAttribute("src", logo_url)
   logo_col_div.appendChild(logo)

   enterprise_info_div = document.createElement("div")
   enterprise_info_div.classList.add("col-md-8", "enterprise-info")
   row.appendChild(enterprise_info_div)
   

   h3 = document.createElement("h3")
   h3.setAttribute("class", "text-primary")
   h3.innerHTML = empresa_name
   enterprise_info_div.appendChild(h3)

   p = document.createElement("p")
   p.classList.add("text-muted")
   p.innerHTML = "Raw denim you probably haven't heard of them jean shorts Austin. Nesciunt tofu stumptown aliqua butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terr."
   enterprise_info_div.appendChild(p)

   br = document.createElement("br")
   div1.appendChild(br)

   div2 = document.createElement("div")
   div2.classList.add("text-muted")
   div1.appendChild(div2)

   p2 = document.createElement("p")
   p2.classList.add("text-sm")
   p2.innerHTML = "Sector de actividad"
   div2.appendChild(p2)

   b1 = document.createElement("b")
   b1.classList.add("d-block")
   b1.innerHTML = sector_actividad
   p2.appendChild(b1)


   p3 = document.createElement("p")
   p3.classList.add("d-block")
   p3.innerHTML = "Direccion de actividad"
   div2.appendChild(p3)

   b2 = document.createElement("b")
   b2.classList.add("d-block")
   b2.innerHTML = ubicacion
   p3.appendChild(b2)

   h5 = document.createElement("h5")
   h5.classList.add("mt-5", "text-muted")
   h5.innerHTML = "Pais de Operacion"
   div1.appendChild(h5)

   operation_country_list = document.createElement("div")
   operation_country_list.setAttribute("class", "operation-country-list")

   ul = document.createElement("ul")
   ul.setAttribute("class", "list-unstyled")

   list_country_op.forEach(function(country){
      li = document.createElement('li')
      li.setAttribute("class", "list-text-secondary")
      li.innerHTML += country
      ul.appendChild(li)
   });
   div1.appendChild(ul)


   detail_url = create_detail_url(obj_absolute_url)

   to_detail = document.createElement("a")
   to_detail.classList.add("text-decoration-none", "call-to-action")
   to_detail.setAttribute("href", detail_url)
   to_detail.setAttribute("target", "_blank")
   to_detail.innerHTML = "Saber más"
   div1.appendChild(to_detail)

   icon = document.createElement("span")
   icon.innerHTML = " ⟶"
   to_detail.appendChild(icon)

   

   card_detalle = document.getElementById("ModalBody")
   card_detalle.appendChild(div1)

   return card_detalle

}

$('.select2').select2({
   theme: 'bootstrap4',
   language: 'es',
   placeholder: "Seleccione una Opcion",
}).select2('data', null)


$("#FilterForm input, select").change(function (e){
   form_data = $("#FilterForm").serialize();
   get_datatable(get_list_url(1, form_data))

});

$(document).on("click", ".page-link", function (e) {
   e.preventDefault();
   let url = $(this).attr("data-url");

   $('body,html').animate({
      scrollTop: 0
   }, 600);

   get_datatable(url);

})

$(".clear-filters").on("click", function(e){
   $("#FilterForm").trigger("reset");
   get_datatable(get_list_url(1));

});

$('#EmpresaList tbody').on('click', 'tr', function () {
   var tr_id = $(this).attr('id')
   var obj_data = document.getElementById(tr_id);
   card_detail = create_card_info(obj_data);

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
