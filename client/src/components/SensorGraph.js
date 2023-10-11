import React from 'react';
import { MDBCard, MDBCardBody, MDBCardTitle, MDBLine } from 'mdb-react-ui-kit';

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
          <MDBLine data={{ labels: sensorData.labels, datasets: [{ data: sensorData.temperature, label: 'Temperature', borderColor: '#8884d8' }] }} options={options} />
        </MDBCardBody>
      </MDBCard>

      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Humidity (%)</MDBCardTitle>
          <MDBLine data={{ labels: sensorData.labels, datasets: [{ data: sensorData.humidity, label: 'Humidity', borderColor: '#82ca9d' }] }} options={options} />
        </MDBCardBody>
      </MDBCard>

      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Soil Moisture (%)</MDBCardTitle>
          <MDBLine data={{ labels: sensorData.labels, datasets: [{ data: sensorData.soil, label: 'Soil Moisture', borderColor: '#ff7300' }] }} options={options} />
        </MDBCardBody>
      </MDBCard>

      <MDBCard style={{ marginBottom: '1rem' }}>
        <MDBCardBody>
          <MDBCardTitle>Light (lux)</MDBCardTitle>
          <MDBLine data={{ labels: sensorData.labels, datasets: [{ data: sensorData.light, label: 'Light', borderColor: '#f34c56' }] }} options={options} />
        </MDBCardBody>
      </MDBCard>
    </div>
  );
}

export default SensorGraphs;
