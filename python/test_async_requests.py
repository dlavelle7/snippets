from async_requests import make_async_requests

from asynctest import TestCase, patch, MagicMock, CoroutineMock, call, Mock


class TestAsyncRequests(TestCase):

    @patch('async_requests.ClientSession.__aenter__')
    async def test_make_async_requests(self, mock_session_context):
        mock_get_json = CoroutineMock(
            side_effect=[
                {"count": 1, "id": 1},
                {"count": 1, "id": 2},
                {"count": 1, "id": 3},
            ]
        )
        mock_get_response = MagicMock()
        # async context managers utilize __aenter__()
        mock_get_response.__aenter__.return_value = MagicMock(
            json=mock_get_json)

        mock_get = MagicMock(return_value=mock_get_response)
        mock_session = MagicMock(get=mock_get)
        mock_session_context.return_value = mock_session

        actual = await make_async_requests(['foo', 'bar', 'spam'])

        # Assert mock get called with expected urls
        expected_calls = [
            call('foo', params={}),
            call('bar', params={}),
            call('spam', params={})
        ]
        self.assertEqual(expected_calls, mock_get.call_args_list)
