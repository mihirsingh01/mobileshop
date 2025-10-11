import React from 'react';

const DataTable = ({ data, title }) => {
  if (!data) {
    return <div className="text-center py-8">Loading...</div>;
  }

  if (!Array.isArray(data) || data.length === 0) {
    return (
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4">{title}</h2>
        <p>No data available.</p>
      </div>
    );
  }

  const keys = Object.keys(data[0]);

  return (
    <div className="bg-white shadow rounded-lg overflow-hidden">
      <div className="px-6 py-4 bg-gray-50 border-b">
        <h2 className="text-2xl font-bold text-gray-800">{title}</h2>
      </div>
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              {keys.map((key) => (
                <th
                  key={key}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  {key}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {data.map((item, index) => (
              <tr key={index} className="hover:bg-gray-50">
                {keys.map((key) => (
                  <td key={key} className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    {typeof item[key] === 'object' ? JSON.stringify(item[key]) : item[key]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DataTable;
