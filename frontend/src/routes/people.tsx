import { Form, useLoaderData } from 'react-router-dom';
import api from '../utils/api';
import { Alert, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TextField } from '@mui/material';
import replaceEmptyString from '../utils/utils';

export type PersonData = {
    id: number,
    first_name: string;
    last_name: string;
    address: string;
    license: string;
    dob: Date;
};

export async function loader({ request }) {
    const url = new URL(request.url)
    const searchName = url.searchParams.get("name")
    const searchLicense = url.searchParams.get("license")

    if (searchName !== null && searchLicense !== null) {
        throw new Error("can only search by name or license");
    } else if (searchName !== null) {
        const people = await api.get(`/api/people/?name=${searchName}`).then((res) => res.data);
        let notFound: boolean = false;
        if (people.length === 0) {
            notFound = true
        }
        return { people, notFound }
    } else if (searchLicense !== null) {
        const people = await api.get(`/api/people/?license=${searchLicense}`).then((res) => res.data);
        let notFound: boolean = false;
        if (people.length === 0) {
            notFound = true
        }
        return { people, notFound }
    } else {
        const people = await api.get(`/api/people/`).then((res) => res.data);
        return { people, notfound: false }
    }
}

const People = () => {
    const { people, notFound } = useLoaderData() as { people: PersonData[], notFound: boolean }
    console.log(people)

    return (
        <>
            <Form className='mr-2 mb-2 inline-block'>
                <TextField name='name' id="outlined-basic" label="name" variant="outlined" />
            </Form>
            <Form className='ml-2 mb-2 inline-block'>
                <TextField name='license' id="outlined-basic" label="license" variant="outlined" />
            </Form>
            {notFound && <Alert severity="warning">Not found this person.</Alert>}
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>License</TableCell>
                            <TableCell align="right">Name</TableCell>
                            <TableCell align="right">Address</TableCell>
                            <TableCell align="right">Date of Birth</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {people.map((person: PersonData) => (
                            <TableRow
                                key={person.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell component="th" scope="row">{replaceEmptyString(person.license, 'null')}</TableCell>
                                <TableCell align="right">
                                    {person.first_name + ' ' + person.last_name}
                                </TableCell>
                                <TableCell align="right">{person.address}</TableCell>
                                <TableCell align="right">{String(person.dob)}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    )
}

export default People