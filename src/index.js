import autoComplete from "@tarekraafat/autocomplete.js";
require("regenerator-runtime/runtime");

const selectField = document.querySelector("#id_customer");
const inputField = document.createElement("input");
inputField.id = "id_customer";
inputField.setAttribute("type", "text");
selectField.replaceWith(inputField);

const autoCompleteJS = new autoComplete({
  data: {
    src: async () => {
      const query = document.querySelector("#id_customer").value;
      const source = await fetch(
        "https://127.0.0.1:8000/customer/autocomplete"
      );
      const data = await source.json();
      console.log(data);
      return data.results;
    },
    key: ["results"],
    cache: false,
  },
  trigger: ["input", "focus"],
  noResults: (dataFeedback, generateList) => {
    // Generate autoComplete List
    generateList(autoCompleteJS, dataFeedback, dataFeedback.results);
    // No Results List Item
    const result = document.createElement("li");
    result.setAttribute("class", "no_result");
    result.setAttribute("tabindex", "1");
    result.innerHTML = `<span style="display: flex; align-items: center; font-weight: 100; color: rgba(0,0,0,.2);">Found No Results for "${dataFeedback.query}"</span>`;
    document
      .querySelector(`#${autoCompleteJS.resultsList.idName}`)
      .appendChild(result);
  },
});
