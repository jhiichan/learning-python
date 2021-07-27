import React, { useState, useEffect } from 'react'
import styled from 'styled-components'
import axios from 'axios'

import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import { default as MatCard } from '@material-ui/core/Card'
import CardHeader from '@material-ui/core/CardHeader'
import CardContent from '@material-ui/core/CardContent'

const Container = styled.div`
    margin: 0 5px;
`

const FilterContainer = styled.div`
    text-align: center;
`

const CardContainer = styled.div`
    text-align: center;
    display: flex;
    flex-direction: row;
`

const Card = styled(MatCard)`
    width: 300px;
    margin: 5px;
`

const ShowsPage = () => {
    const [searchKeyword, setSearchKeyword] = useState('');
    const [showsData, setShowsData] = useState([]);

    const handleSearchKeywordChange = (event) => {
        setSearchKeyword(event.target.value)
    };

    useEffect(() => {
        getAllShows();
    },[]);

    useEffect(() => {
        console.log(showsData);
    },[showsData]);

    const getAllShows = async () => {
        await axios.get('http://localhost:3030/show/').then(({data}) => {
            setShowsData(data);
        });
    }

    return (
        <Container>
            <Typography variant='h1'>Shows</Typography>
            <FilterContainer>
                <TextField id='search-keyword' name='Search' label='Search' value={searchKeyword} onChange={handleSearchKeywordChange} />
                <Button variant='contained' color='primary'>Search</Button>
            </FilterContainer>
            <CardContainer>
                {/* <Card>
                    <CardHeader title={title} />
                    <CardContent>
                        <Typography variant='body1'>Testing</Typography>
                    </CardContent>
                </Card> */}
            </CardContainer>
        </Container>
    )
}

export default ShowsPage
