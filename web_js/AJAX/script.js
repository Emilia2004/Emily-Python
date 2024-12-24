document.addEventListener('DOMContentLoaded', function () {
    const searchBar = document.getElementById('searchBar');
    const profilesContainer = document.getElementById('profiles');
    let profilesData = [];
  
    fetch('data.json')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        profilesData = data.people; 
        displayProfiles(profilesData);
      })
      .catch((error) => {
        console.error('Error loading data:', error);
        profilesContainer.innerHTML = '<p class="error">Failed to load profiles. Please try again later.</p>';
      });
  

    function displayProfiles(profiles) {
      profilesContainer.innerHTML = profiles
        .map(
          (person) => `
            <div class="card">
                <img src="${person.photo}" alt="${person.name}">
                <h2>${person.name} ${person.surname}</h2>
                <p>Age: ${person.age}</p>
                <p>Sex: ${person.sex}</p>
            </div>
        `
        )
        .join('');
    }
  
    searchBar.addEventListener('input', function (e) {
      const searchValue = e.target.value.toLowerCase();
      const filteredProfiles = profilesData.filter(
        (person) =>
          person.name.toLowerCase().includes(searchValue) ||
          person.surname.toLowerCase().includes(searchValue)
      );
      displayProfiles(filteredProfiles);
    });
  });
  