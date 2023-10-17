import React from 'react';
import { MDBCard, MDBCardBody, MDBCardTitle } from 'mdb-react-ui-kit';
import { Line } from 'react-chartjs-2';  // Imported Line from react-chartjs-2

function SensorGraphs({ sensorData }) {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
  };

  return (
    <div>
      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Temperature (°F)</MDBCardTitle>
          <Line data={{ labels: sensorData.labels, datasets: [{ data: sensorData.temperature, label: 'Temperature', borderColor: '#8884d8', fill: false }] }} options={options} />
        </MDBCardBody>
      </MDBCard>

      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Humidity (%)</MDBCardTitle>
          <Line data={{ labels: sensorData.labels, datasets: [{ data: sensorData.humidity, label: 'Humidity', borderColor: '#82ca9d', fill: false }] }} options={options} />
        </MDBCardBody>
      </MDBCard>

      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Soil Moisture (%)</MDBCardTitle>
          <Line data={{ labels: sensorData.labels, datasets: [{ data: sensorData.soil, label: 'Soil Moisture', borderColor: '#ff7300', fill: false }] }} options={options} />
        </MDBCardBody>
      </MDBCard>

      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Light (lux)</MDBCardTitle>
          <Line data={{ labels: sensorData.labels, datasets: [{ data: sensorData.light, label: 'Light', borderColor: '#f34c56', fill: false }] }} options={options} />
        </MDBCardBody>
      </MDBCard>
    </div>
  );
}

export default SensorGraphs;
