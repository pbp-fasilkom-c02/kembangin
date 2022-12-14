$(document).ready(() => {
    const card = data => `
      <div
        class="card flex justify-center ${
          data.fields.status && "opacity-50"
        } hover:scale-105 transition-all"
      >
        <div
          class="block rounded-lg shadow-lg hover:shadow-blue-500/30 bg-white max-w-sm text-center w-80"
        >
          <div
            class="py-3 px-6 border-b bg-red-400 flex gap-4 text-white justify-center form-check items-center rounded-t-lg hover:bg-gradient-to-bl transition-all"
          >
            <label for="status inline-block">BMI Metric</label>
          </div>
          <div class="p-6"> 
            <h5 class="text-gray-900 text-xl font-bold mb-2">BMI : ${
              data.fields.bmi 
            }</h5>
            <p class="text-gray-700 text-sm mb-4">Weight : ${data.fields.weight} kg</p>
            <p class="text-gray-700 text-sm mb-4">Height : ${data.fields.height} cm</p>
            <a href="/bmicalculator/delete/${data.pk}/">
            <button
              type="button"
              class="inline-block mx-auto  px-6 pt-2.5 pb-2 transition duration-150 ease-in-out flex align-center gap-2 items-center text-white bg-gradient-to-r from-pink-500 to-red-500 hover:bg-gradient-to-r focus:ring-4 focus:outline-none focus:ring-pink-300 rounded-lg px-5 py-2.5"
            >
              Delete
            </button>
            </a>
          </div>
          <div class="py-3 px-6 border-t border-gray-300 text-gray-600">
            <p class="text-xs">Created At:</p>
            <p>${data.fields.date}</p>
          </div>
          <div class="py-3 px-6 border-t border-gray-300 text-gray-600">
            <p class="text-xs">Created By:</p>
            <p>${data.fields.author}</p>
            
          </div>
        </div>
      </div>
    `;
  
    const renderTasks = () => {
      // fetching the tasks
      $.get("/bmicalculator/json/", data => {
        data.sort((a, b) => {
          return a.fields.status - b.fields.status;
        });
        $.each(data, (i, value) => {
          $("#bmicalculator").append(card(value)); // append to the div
  
          // add event listener to the delete button
          $(`#delete-${value.pk}`).click(() => {
            deleteTask(value.pk);
          });
        });
      });
      
    };
  
    const deleteTask = id => {
      // get the CSRF Token
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
  
      $.ajax({
        url: `/bmicalculator/delete/${id}/`,
        type: "DELETE",
        headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
        mode: "same-origin", // Do not send CSRF token to another domain.
        success: () => {
          // remove the card
          $(`#delete-${id}`).parent().parent().parent().remove();
        },
        error: error => {
          console.log(error);
        },
      });
    };
  
    const openModal = e => {
      e.preventDefault(); // prevent refresh
      $("#create-data-modal").removeClass("hidden");
    };
  
    const closeModal = e => {
      // e.preventDefault(); // prevent refresh
      $("#create-data-modal").addClass("hidden");
    };
  
    $("#create-data-form").submit(e => {
      e.preventDefault();
  
      // get the CSRF Token
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
  
      const weight = $("#weight").val();
      const height = $("#height").val();
  
      if (weight && height) {
        $.ajax({
          type: "POST",
          url: "/bmicalculator/add/",
          headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
          mode: "same-origin", // Do not send CSRF token to another domain.
          data: {
            weight: weight,
            height: height,
          },
          success: response => {
            $("#create-data-form").trigger("reset");
            closeModal();
            $("#bmicalculator").prepend(card(response));
            console.log(response);
            // $(`#delete-${response.pk}`).click(() => {
            //   deleteTask(response.pk);
            // });
          },
          error: error => {
            console.log(error);
          },
        });
      } else {
        alert("Please fill all the fields");
      }
    });
  
    $("#create-data").click(openModal);
    $("#close-modal").click(closeModal);
  
    renderTasks();
  });