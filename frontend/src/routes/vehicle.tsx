import { Form, useLoaderData } from 'react-router-dom';
import api from '../utils/api';
import { Alert, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TextField } from '@mui/material';
import { PersonData } from './people';
import replaceEmptyString from '../utils/utils';

export type VehicleData = {
  id: number,
  make: string,
  color: string,
  model: string,
  plate_number: string
};

export type OwnershipData = {
  id: number,
  vehicle?: VehicleData,
  people?: PersonData
}

export async function loader({ request }) {
  const url = new URL(request.url)
  const searchPlate_number = url.searchParams.get('plate_number')
  if (searchPlate_number !== null) {
    const ownerships = await api.get(`/api/ownership/?plate_number=${searchPlate_number}`).then((res) => res.data)
    let notFound = false;
    if (ownerships.length === 0) {
      notFound = true
    }
    return { ownerships, notFound }
  } else {
    const ownerships = await api.get(`/api/ownership/`).then((res) => res.data);
    return { ownerships, notfound: false }
  }
}

const Vehicle = () => {
  const { ownerships, notFound } = useLoaderData() as { ownerships: OwnershipData[], notFound: boolean }
  console.log(ownerships)

  return (
    <>
      <Form className='mb-2'>
        <TextField name='plate_number' id="outlined-basic" label="plate number" variant="outlined" />
      </Form>
      {notFound && <Alert severity="warning">Not found this vehicle.</Alert>}
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Plate Number</TableCell>
              <TableCell align="right">Make</TableCell>
              <TableCell align="right">Model</TableCell>
              <TableCell align="right">Color</TableCell>
              <TableCell align="right">Owner Name</TableCell>
              <TableCell align="right">Owner License</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {ownerships.map(({ vehicle, people: person, id }: OwnershipData) => (
              <TableRow
                key={id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">{vehicle && vehicle.plate_number ? replaceEmptyString(vehicle.plate_number, 'null') : 'unknown'}</TableCell>
                <TableCell align="right">{vehicle ? vehicle.make : 'unknown'}</TableCell>
                <TableCell align="right">{vehicle ? vehicle.model : 'unknown'}</TableCell>
                <TableCell align="right">{vehicle ? vehicle.color : 'unknown'}</TableCell>
                <TableCell align="right">{person ? person.first_name + ' ' + person.last_name : 'unknown'}</TableCell>
                <TableCell align="right">{person ? replaceEmptyString(person.license, 'null') : 'unknown'}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  )
}

export default Vehicle