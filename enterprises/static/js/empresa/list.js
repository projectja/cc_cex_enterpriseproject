get_datatable();

function get_datatable (data) {

   $('#EmpresaList').DataTable({
      responsive: true,
      autoWidth: false,
      destroy: true,
      deferRender: true,
      ajax: {
          url: window.location.pathname,
          type: 'POST',
          data: data,
          dataSrc: ""
      },
      columns: [
          {"data": "nombre"},
          {"data": "poblacion.nombre"},
          {"data": "partidas"},
      ]
  });

}

$("#btnFilter").click(function (){
   var poblacion = $("#id_poblacion");
   var sector = $("#id_sector");
   var alpha = $("#id_alpha");

   data  = {
      'poblacion': poblacion.val(),
      'sector': sector.val(),
      'alpha': alpha.val(),
   }

   get_datatable(data);

});


$('#EmpresaList tbody').on('click', 'tr', function () {
   var table = $("#EmpresaList").DataTable();
   var data = table.row(this).data();
   
   $(".info-text").css("display", "none");

   create_card_info(data);
});


function create_card_info(data){
   // Create a card where enterprise
   // info goes.
   $("#cardEmpresaDetalle").html("")

   // div with card class.
   card = document.createElement('div')
   card.classList.add("card", "detalle-empresa", "mt-5")

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
   title.innerHTML = data.nombre

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
   b1.innerHTML = data.poblacion.nombre

   p3 = document.createElement("p")
   p3.classList.add("d-block")
   p3.innerHTML = "Partidas"

   b2 = document.createElement("b")
   b2.classList.add("d-block")
   b2.innerHTML = data.partidas

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

   card_detalle = document.getElementById("cardEmpresaDetalle")
   card_detalle.appendChild(card)

}




    




