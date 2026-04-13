const submitButton = document.getElementById('submit-button');
const tableBody = document.getElementById('table-body');
const section = document.querySelector('section');

const API_URL = 'http://localhost:3001';


async function loadWaters() {
  try {
    const response = await fetch(`${API_URL}/waters`);
    const data = await response.json();
    tableBody.innerHTML = '';
    data.waters.forEach(appendRow);
  } catch (err) {
    console.error('Erro ao carregar amostras:', err);
  }
}

function goToBottom() {
  window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
}

async function addWater() {
  const body = {
    ph: parseFloat(document.querySelector('[name="ph"]').value),
    hardness: parseFloat(document.querySelector('[name="hardness"]').value),
    solids: parseFloat(document.querySelector('[name="solids"]').value),
    chloramines: parseFloat(document.querySelector('[name="chloramines"]').value),
    sulfate: parseFloat(document.querySelector('[name="sulfate"]').value),
    conductivity: parseFloat(document.querySelector('[name="conductivity"]').value),
    organic_carbon: parseFloat(document.querySelector('[name="organic_carbon"]').value),
    trihalomethanes: parseFloat(document.querySelector('[name="trihalomethanes"]').value),
    turbidity: parseFloat(document.querySelector('[name="turbidity"]').value),
  };

  try {
    const response = await fetch(`${API_URL}/waters`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const err = await response.json();
      alert('Erro: ' + err.message);
      return;
    }

    const water = await response.json();
    changePotabilityClass(water.potability);
    appendRow(water);

   
    
    goToBottom();

  } catch (err) {
    console.error('Erro ao adicionar amostra:', err);
    alert('Erro ao conectar com a API.');
  }
}

async function deleteWater(id) {
  try {
    const response = await fetch(`${API_URL}/waters/${id}`, { method: 'DELETE' });

    if (!response.ok) {
      const err = await response.json();
      alert('Erro: ' + err.message);
      return;
    }

    document.getElementById(`row-${id}`).remove();
  } catch (err) {
    console.error('Erro ao deletar amostra:', err);
    alert('Erro ao conectar com a API.');
  }
}

function changePotabilityClass(potability) {
 
  section.classList.remove('potable', 'non-potable');
  section.classList.add(potability ? 'potable' : 'non-potable');
}

function appendRow(water) {
  const row = document.createElement('tr');
  row.id = `row-${water.id}`;

  const potabilidade = water.potability ? 'Potável' : 'Não potável';
  const potClass = water.potability ? 'potable' : 'not-potable';

  row.innerHTML = `
    <td>${water.id}</td>
    <td>${water.ph}</td>
    <td>${water.hardness}</td>
    <td>${water.solids}</td>
    <td>${water.chloramines}</td>
    <td>${water.sulfate}</td>
    <td>${water.conductivity}</td>
    <td>${water.organic_carbon}</td>
    <td>${water.trihalomethanes}</td>
    <td>${water.turbidity}</td>
    <td class="${potClass}">${potabilidade}</td>
    <td class="content__table-action"><i class="fas fa-trash" onclick="deleteWater(${water.id})"></i></td>
  `;

  tableBody.appendChild(row);
}


document.addEventListener('DOMContentLoaded', loadWaters);
section.addEventListener('load', goToBottom);
submitButton.addEventListener('click', addWater);