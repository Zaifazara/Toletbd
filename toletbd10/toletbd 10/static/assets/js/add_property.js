document.addEventListener("DOMContentLoaded", function () {
  function handleRadioChange(radio, fieldsArray) {
    radio.addEventListener("change", function () {
      fieldsArray.forEach(fields => {
        fields.style.display = "none";
      });

      if (radio.checked) {
        const selectedFields = fieldsArray.find(fields => fields.id === radio.id.replace("Same", ""));
        if (selectedFields) {
          selectedFields.style.display = "block";
        }
      }
    });
  }

  const radioFieldPairs = [
    { radio: document.getElementById("FamilySame"), fields: document.getElementById("Family") },
    { radio: document.getElementById("SubletSame"), fields: document.getElementById("Sublet") },
    { radio: document.getElementById("BachelorSame"), fields: document.getElementById("Bachelor") },
    { radio: document.getElementById("HostelSame"), fields: document.getElementById("Hostel") },
    { radio: document.getElementById("OfficeSame"), fields: document.getElementById("Office") },
    { radio: document.getElementById("ShopSame"), fields: document.getElementById("Shop") },
  ];

  // Attach event listeners to the radio buttons
  radioFieldPairs.forEach(pair => {
    if (pair.radio) {
      handleRadioChange(pair.radio, radioFieldPairs.map(item => item.fields));
    }
  });
});




document.addEventListener("DOMContentLoaded", function () {
  // ... your existing code ...

  // Function to update districts based on the selected country
  function updateDistricts(divisionId) {
      $.ajax({
          url: '/get-districts/',
          data: { 'division_id': divisionId },
          dataType: 'json',
          success: function (data) {
              const districtSelect = document.getElementById('state');
              districtSelect.innerHTML = '<option selected>Choose District</option>';
              data.districts.forEach(function (district) {
                  const option = document.createElement('option');
                  option.value = district.id;
                  option.text = district.name;
                  districtSelect.add(option);
              });
          }
      });
  }

  // Function to update upazilas based on the selected district
  function updateUpazilas(districtId) {
      $.ajax({
          url: '/get-upazilas/',
          data: { 'district_id': districtId },
          dataType: 'json',
          success: function (data) {
              const upazilaSelect = document.getElementById('district');
              upazilaSelect.innerHTML = '<option selected>Choose Upazila</option>';
              data.upazilas.forEach(function (upazila) {
                  const option = document.createElement('option');
                  option.value = upazila.id;
                  option.text = upazila.name;
                  upazilaSelect.add(option);
              });
          }
      });
  }

  // Attach event listeners to the country and district dropdowns
  const divisionSelect = document.getElementById('country');
  const districtSelect = document.getElementById('state');

  divisionSelect.addEventListener('change', function () {
      const divisionId = this.value;
      if (divisionId) {
          updateDistricts(divisionId);
      }
  });

  districtSelect.addEventListener('change', function () {
      const districtId = this.value;
      if (districtId) {
          updateUpazilas(districtId);
      }
  });

  // ... your existing code ...
});